1. src/main/java/im/zhaojun/zfile/module/readme/service/ReadmeConfigService.java
```
package im.zhaojun.zfile.module.readme.service;

import cn.hutool.core.collection.CollUtil;
import cn.hutool.core.util.BooleanUtil;
import cn.hutool.core.util.StrUtil;
import im.zhaojun.zfile.module.storage.context.StorageSourceContext;
import im.zhaojun.zfile.core.util.HttpUtil;
import im.zhaojun.zfile.core.util.PatternMatcherUtils;
import im.zhaojun.zfile.core.util.StringUtils;
import im.zhaojun.zfile.module.readme.mapper.ReadmeConfigMapper;
import im.zhaojun.zfile.module.readme.model.entity.ReadmeConfig;
import im.zhaojun.zfile.module.readme.model.enums.ReadmeDisplayModeEnum;
import im.zhaojun.zfile.module.storage.model.param.IStorageParam;
import im.zhaojun.zfile.module.storage.model.result.FileItemResult;
import im.zhaojun.zfile.module.storage.service.base.AbstractBaseFileService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;
import java.util.List;

/**
 * 存储源 readme 配置 Service
 *
 * @author zhaojun
 */
@Slf4j
@Service
@CacheConfig(cacheNames = "readmeConfig")
public class ReadmeConfigService {

	@Resource
	private ReadmeConfigMapper readmeConfigMapper;
	
	@Resource
	private ReadmeConfigService readmeConfigService;
	
	@Resource
	private StorageSourceContext storageSourceContext;

	/**
	 * 根据存储源 ID 查询文档配置
	 *
	 * @param   storageId
	 *          存储源ID
	 *
	 * @return  存储源文档配置列表
	 */
	@Cacheable(key = "#storageId")
	public List<ReadmeConfig> findByStorageId(Integer storageId){
		return readmeConfigMapper.findByStorageId(storageId);
	}


	/**
	 * 批量保存存储源 readme 配置, 会先删除之前的所有配置(在事务中运行)
	 *
	 * @param   storageId
	 *          存储源 ID
	 *
	 * @param   readmeConfigList
	 *          存储源 readme 配置列表
	 */
	@Transactional(rollbackFor = Exception.class)
	public void batchSave(Integer storageId, List<ReadmeConfig> readmeConfigList) {
		readmeConfigService.deleteByStorageId(storageId);
		
		log.info("更新存储源 ID 为 {} 的目录文档配置 {} 条", storageId, readmeConfigList.size());
		
		readmeConfigList.forEach(readmeConfig -> {
			readmeConfig.setStorageId(storageId);
			readmeConfigMapper.insert(readmeConfig);
			
			if (log.isDebugEnabled()) {
				log.debug("新增目录文档, 存储源 ID: {}, 表达式: {}, 描述: {}, 显示模式: {}",
						readmeConfig.getStorageId(), readmeConfig.getExpression(),
						readmeConfig.getDescription(), readmeConfig.getDisplayMode().getValue());
			}
		});
	}
	
	
	/**
	 * 根据存储源 ID 删除存储源 readme 配置
	 *
	 * @param 	storageId
	 * 			存储源 ID
	 */
	@CacheEvict(key = "#storageId")
	public int deleteByStorageId(Integer storageId) {
		int deleteSize = readmeConfigMapper.deleteByStorageId(storageId);
		log.info("删除存储源 ID 为 {} 的目录文档配置 {} 条", storageId, deleteSize);
		return deleteSize;
	}


	/**
	 * 根据存储源指定路径下的 readme 配置
	 *
	 * @param   storageId
	 *          存储源ID
	 *
	 * @param   path
	 *          文件夹路径
	 *
	 * @return  存储源 readme 配置列表
	 */
	public ReadmeConfig findReadmeByPath(Integer storageId, String path) {
		List<ReadmeConfig> readmeConfigList = readmeConfigService.findByStorageId(storageId);
		return getReadmeByTestPattern(storageId, readmeConfigList, path);
	}
	
	
	/**
	 * 根据存储源指定路径下的 readme 配置，如果指定为兼容模式，则会读取指定目录下的 readme.md 文件.
	 *
	 * @param 	storageId
	 * 			存储源 ID
	 *
	 * @param 	path
	 * 			存储源路径
	 *
	 * @param 	compatibilityReadme
	 * 			是否兼容为读取 readme.md 文件
	 *
	 * @return  目录下存储源 readme 配置
	 */
	public ReadmeConfig getByStorageAndPath(Integer storageId, String path, Boolean compatibilityReadme) {
		ReadmeConfig readmeByPath = new ReadmeConfig();
		readmeByPath.setStorageId(storageId);
		readmeByPath.setDisplayMode(ReadmeDisplayModeEnum.BOTTOM);
		if (BooleanUtil.isTrue(compatibilityReadme)) {
			try {
				log.info("存储源 {} 兼容获取目录 {} 下的 readme.md", storageId, path);
				AbstractBaseFileService<IStorageParam> abstractBaseFileService = storageSourceContext.getByStorageId(storageId);
				String pathAndName = StringUtils.concat(path, "readme.md");
				FileItemResult fileItem = abstractBaseFileService.getFileItem(pathAndName);
				if (fileItem != null) {
					String url = fileItem.getUrl();
					String readmeText = HttpUtil.getTextContent(url);
					readmeByPath.setReadmeText(readmeText);
				}
			} catch (Exception e) {
				log.error("存储源 {} 兼容获取目录 {} 下的 readme.md 文件失败", storageId, path, e);
			}
		} else {
			// 获取指定目录 readme 文件
			ReadmeConfig dbReadmeConfig = readmeConfigService.findReadmeByPath(storageId, path);
			if (dbReadmeConfig != null) {
				readmeByPath = dbReadmeConfig;
			}
			log.info("存储源 {} 规则模式获取目录 {} 下文档信息", storageId, path);
		}
		
		return readmeByPath;
	}
	

	/**
	 * 根据规则表达式和测试字符串进行匹配，如测试字符串和其中一个规则匹配上，则返回 true，反之返回 false。
	 *
	 * @param   patternList
	 *          规则列表
	 *
	 * @param   test
	 *          测试字符串
	 *
	 * @return  是否显示
	 */
	private ReadmeConfig getReadmeByTestPattern(Integer storageId, List<ReadmeConfig> patternList, String test) {
		// 如果目录文档规则为空, 则可直接返回空.
		if (CollUtil.isEmpty(patternList)) {
			if (log.isDebugEnabled()) {
				log.debug("目录文档规则列表为空, 存储源 ID: {}, 测试字符串: {}", storageId, test);
			}
			return null;
		}
		
		for (ReadmeConfig filterConfig : patternList) {
			String expression = filterConfig.getExpression();
			
			if (StrUtil.isEmpty(expression)) {
				if (log.isDebugEnabled()) {
					log.debug("存储源 {} 目录文档规则表达式为空: {}, 测试字符串: {}, 表达式为空，跳过该规则比对", storageId, expression, test);
				}
				continue;
			}
			
			try {
				boolean match = PatternMatcherUtils.testCompatibilityGlobPattern(expression, test);
				
				if (log.isDebugEnabled()) {
					log.debug("存储源 {} 目录文档规则表达式: {}, 测试字符串: {}, 匹配结果: {}", storageId, expression, test, match);
				}
				
				if (match) {
					return filterConfig;
				}
			} catch (Exception e) {
				log.error("存储源 {} 目录文档规则表达式: {}, 测试字符串: {}, 匹配异常，跳过该规则.", storageId, expression, test, e);
			}
		}

		return null;
	}
	

}
```
2.  src/main/java/im/zhaojun/zfile/module/storage/context/StorageSourceContext.java
```
package im.zhaojun.zfile.module.storage.context;

import cn.hutool.core.util.BooleanUtil;
import cn.hutool.core.util.ReflectUtil;
import cn.hutool.core.util.StrUtil;
import cn.hutool.extra.spring.SpringUtil;
import im.zhaojun.zfile.core.config.FlywayDbInitializer;
import im.zhaojun.zfile.core.exception.file.InvalidStorageSourceException;
import im.zhaojun.zfile.core.exception.file.init.InitializeStorageSourceException;
import im.zhaojun.zfile.core.util.ClassUtils;
import im.zhaojun.zfile.core.util.CodeMsg;
import im.zhaojun.zfile.module.storage.annotation.StorageParamItem;
import im.zhaojun.zfile.module.storage.model.bo.StorageSourceParamDef;
import im.zhaojun.zfile.module.storage.model.entity.StorageSource;
import im.zhaojun.zfile.module.storage.model.entity.StorageSourceConfig;
import im.zhaojun.zfile.module.storage.model.enums.StorageTypeEnum;
import im.zhaojun.zfile.module.storage.model.param.IStorageParam;
import im.zhaojun.zfile.module.storage.service.StorageSourceConfigService;
import im.zhaojun.zfile.module.storage.service.StorageSourceService;
import im.zhaojun.zfile.module.storage.service.base.AbstractBaseFileService;
import im.zhaojun.zfile.module.storage.service.base.RefreshTokenService;
import im.zhaojun.zfile.module.storage.support.StorageSourceSupport;
import lombok.extern.slf4j.Slf4j;
import org.springframework.aop.support.AopUtils;
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.annotation.DependsOn;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;
import java.lang.reflect.Field;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/**
 * 每个存储源对应一个 Service, 其中初始化好了与对象存储的配置信息.
 * 此存储源上下文环境用户缓存每个 Service, 避免重复初始化.
 * <br>
 * 依赖 {@link FlywayDbInitializer} 初始化数据库后执行.
 *
 * @author zhaojun
 */
@Component
@DependsOn("flywayDbInitializer")
@Slf4j
public class StorageSourceContext implements ApplicationContextAware {

    /**
     * Map<Integer, AbstractBaseFileService>
     * Map<存储源 ID, 存储源 Service>
     */
    private static final Map<Integer, AbstractBaseFileService<IStorageParam>> DRIVES_SERVICE_MAP = new ConcurrentHashMap<>();


    /**
     * Map<存储源类型, 存储源 Service>
     */
    private static  Map<String, AbstractBaseFileService> storageTypeEnumFileServiceMap;

    /**
     * 缓存每个存储源参数的字段列表.
     */
    private final Map<Class<?>, Map<String, Field>> PARAM_CLASS_FIELD_NAME_MAP_CACHE = new HashMap<>();


    @Resource
    private StorageSourceService storageSourceService;

    @Resource
    private StorageSourceConfigService storageSourceConfigService;


    /**
     * 项目启动时, 自动调用数据库已存储的所有存储源进行初始化.
     */
    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        storageTypeEnumFileServiceMap = applicationContext.getBeansOfType(AbstractBaseFileService.class);

        List<StorageSource> list = storageSourceService.findAllOrderByOrderNum();
        for (StorageSource storageSource : list) {
            try {
                init(storageSource);
                log.info("启动时初始化存储源成功, 存储源 id: [{}], 存储源类型: [{}], 存储源名称: [{}]",
                        storageSource.getId(), storageSource.getType().getDescription(), storageSource.getName());
            } catch (Exception e) {
                log.error("启动时初始化存储源失败, 存储源 id: {}, 存储源类型: {}, 存储源名称: {}",
                        storageSource.getId(), storageSource.getType().getDescription(), storageSource.getName(), e);
            }
        }
    }


    /**
     * 根据存储源 id 获取对应的 Service.
     *
     * @param   storageId
     *          存储源 ID
     *
     * @return  存储源对应的 Service
     */
    public AbstractBaseFileService<IStorageParam> getByStorageId(Integer storageId) {
        AbstractBaseFileService<IStorageParam> abstractBaseFileService = DRIVES_SERVICE_MAP.get(storageId);
        if (abstractBaseFileService == null) {
            throw new InvalidStorageSourceException(storageId);
        }
        return abstractBaseFileService;
    }


    /**
     * 根据存储源 key 获取对应的 Service.
     *
     * @param   key
     *          存储源 key
     *
     * @return  存储源对应的 Service
     */
    public AbstractBaseFileService<?> getByStorageKey(String key) {
        Integer storageId = storageSourceService.findIdByKey(key);
        if (storageId == null) {
            return null;
        }
        return getByStorageId(storageId);
    }


    /**
     * 根据存储类型获取对应的存储源的参数列表.
     *
     * @param   type
     *          存储类型: {@link StorageTypeEnum}
     *
     * @return  指定类型存储源的参数列表. {@link StorageSourceSupport#getStorageSourceParamList(AbstractBaseFileService)} )}}
     */
    public static List<StorageSourceParamDef> getStorageSourceParamListByType(StorageTypeEnum type) {
        return storageTypeEnumFileServiceMap.values().stream()
                // 根据存储源类型找到第一个匹配的 Service
                .filter(fileService -> fileService.getStorageTypeEnum() == type)
                .findFirst()
                // 获取该 Service 的参数列表
                .map(StorageSourceSupport::getStorageSourceParamList)
                // 如果没有找到, 则返回空列表
                .orElse(Collections.emptyList());
    }


    /**
     * 初始化指定存储源的 Service, 添加到上下文环境中.
     *
     * @param   storageSource
     *          存储源对象
     */
    public void init(StorageSource storageSource) {
        Integer storageId = storageSource.getId();
        String storageName = storageSource.getName();

        AbstractBaseFileService<IStorageParam> baseFileService = getInitStorageBeanByStorageId(storageId);
        if (baseFileService == null) {
            throw new InvalidStorageSourceException(storageId);
        }

        // 填充初始化参数
        IStorageParam initParam = getInitParam(storageId, baseFileService);

        // 进行初始化并测试连接
        baseFileService.init(storageName, storageId, initParam);
        baseFileService.testConnection();

        DRIVES_SERVICE_MAP.put(storageId, baseFileService);
    }


    /**
     * 获取指定存储源初始状态的 Service.
     *
     * @param   storageId
     *          存储源 ID
     *
     * @return  存储源对应未初始化的 Service
     */
    private AbstractBaseFileService<IStorageParam> getInitStorageBeanByStorageId(Integer storageId) {
        StorageTypeEnum storageTypeEnum = storageSourceService.findStorageTypeById(storageId);
        for (AbstractBaseFileService<?> value : storageTypeEnumFileServiceMap.values()) {
            if (Objects.equals(value.getStorageTypeEnum(), storageTypeEnum)) {
                return SpringUtil.getBean(value.getClass());
            }
        }
        return null;
    }


    /**
     * 获取指定存储源的初始化参数.
     *
     * @param   storageId
     *          存储源 ID
     *
     * @return  存储源初始化参数
     */
    private IStorageParam getInitParam(Integer storageId, AbstractBaseFileService<?> baseFileService) {
        // 获取存储源实现类的实际 Class
        Class<?> beanTargetClass = AopUtils.getTargetClass(baseFileService);
        // 获取存储源实现类的实际 Class 的泛型参数类型
        Class<?> paramClass = ClassUtils.getClassFirstGenericsParam(beanTargetClass);

        // 获取存储器参数 key -> 存储器 field 对照关系，如果缓存中有，则从缓存中取.
        Map<String, Field> fieldMap = new HashMap<>();
        if (PARAM_CLASS_FIELD_NAME_MAP_CACHE.containsKey(paramClass)) {
            fieldMap = PARAM_CLASS_FIELD_NAME_MAP_CACHE.get(paramClass);
        } else {
            Field[] fields = ReflectUtil.getFieldsDirectly(paramClass, true);
            List<String> ignoreFieldNameList = new ArrayList<>();
            for (Field field : fields) {
                String key;

                StorageParamItem storageParamItem = field.getDeclaredAnnotation(StorageParamItem.class);
                // 没有注解或注解中没有配置 key 则使用字段名.
                if (storageParamItem == null || StrUtil.isEmpty(storageParamItem.key())) {
                    key = field.getName();
                } else {
                    key = storageParamItem.key();
                }

                if (storageParamItem.ignoreInput()) {
                    ignoreFieldNameList.add(key);
                }

                // 如果 map 中包含此 key, 则是父类的, 跳过.
                if (fieldMap.containsKey(key)) {
                    continue;
                }

                if (!ignoreFieldNameList.contains(key)) {
                    fieldMap.put(key, field);
                }
            }
            PARAM_CLASS_FIELD_NAME_MAP_CACHE.put(paramClass, fieldMap);
        }

        // 实例化参数对象
        IStorageParam iStorageParam = ReflectUtil.newInstance(paramClass.getName());

        // 给所有字段填充值
        List<StorageSourceConfig> storageSourceConfigList = storageSourceConfigService.selectStorageConfigByStorageId(storageId);
        for (StorageSourceConfig storageSourceConfig : storageSourceConfigList) {
            String name = storageSourceConfig.getName();
            String value = storageSourceConfig.getValue();
            try {
                Field field = fieldMap.get(name);
                ReflectUtil.setFieldValue(iStorageParam, field, value);
            } catch (Exception e) {
                String errMsg = StrUtil.format("为字段 {} 初始化值 {} 失败", name, value);
                throw new InitializeStorageSourceException(CodeMsg.STORAGE_SOURCE_INIT_STORAGE_PARAM_FIELD_FAIL, storageId, errMsg, e).setResponseExceptionMessage(true);
            }
        }

        return iStorageParam;
    }


    /**
     * 获取所有 AccessToken 机制的存储源, 这些存储源都继承类 {@link RefreshTokenService}.
     *
     * @return  获取所有需要刷新 AccessToken 的存储源.
     */
    public Map<Integer, RefreshTokenService> getAllRefreshTokenStorageSource() {
        Map<Integer, RefreshTokenService> result = new HashMap<>();

        for (Map.Entry<Integer, AbstractBaseFileService<IStorageParam>> baseFileServiceEntry : DRIVES_SERVICE_MAP.entrySet()) {
            Integer storageId = baseFileServiceEntry.getKey();
            AbstractBaseFileService<?> baseFileService = baseFileServiceEntry.getValue();
            // 如果未初始化成功, 则直接跳过
            if (BooleanUtil.isFalse(baseFileService.isInitialized())) {
                continue;
            }

            if (baseFileService instanceof RefreshTokenService) {
                result.put(storageId, (RefreshTokenService) baseFileService);
            }
        }

        return result;
    }


    /**
     * 销毁指定存储源的 Service.
     *
     * @param   storageId
     *          存储源 ID
     */
    public void destroy(Integer storageId) {
        log.info("清理存储源上下文对象, storageId: {}", storageId);
        DRIVES_SERVICE_MAP.remove(storageId);
    }


}

```
3.  src/main/java/im/zhaojun/zfile/module/storage/service/impl/GoogleDriveServiceImpl.java:414-451
```
	/**
	 * 转换 api 返回的 json object 为 zfile 文件对象
	 *
	 * @param 	jsonObject
	 * 			api 返回文件 json object
	 *
	 * @param 	folderPath
	 * 			所属文件夹路径
	 *
	 * @return	zfile 文件对象
	 */
	public FileItemResult jsonObjectToFileItem(JSONObject jsonObject, String folderPath) {
		FileItemResult fileItemResult = new FileItemResult();
		fileItemResult.setName(jsonObject.getString("name"));
		fileItemResult.setPath(folderPath);
		fileItemResult.setSize(jsonObject.getLong("size"));

		String mimeType = jsonObject.getString("mimeType");
		if (ObjectUtil.equals(SHORTCUT_MIME_TYPE, mimeType)) {
			JSONObject shortcutDetails = jsonObject.getJSONObject("shortcutDetails");
			mimeType = shortcutDetails.getString("targetMimeType");
		}

		if (StrUtil.equals(mimeType, FOLDER_MIME_TYPE)) {
			fileItemResult.setType(FileTypeEnum.FOLDER);
		} else {
			fileItemResult.setType(FileTypeEnum.FILE);
			fileItemResult.setUrl(getDownloadUrl(StringUtils.concat(folderPath, fileItemResult.getName())));
		}

		fileItemResult.setTime(jsonObject.getDate("modifiedTime"));

		if (fileItemResult.getSize() == null) {
			fileItemResult.setSize(-1L);
		}

		return fileItemResult;
	}
```

4. src/main/java/im/zhaojun/zfile/ZfileApplication.java
```
package im.zhaojun.zfile;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.EnableAspectJAutoProxy;


/**
 * @author zhaojun
 */
@SpringBootApplication
@EnableAspectJAutoProxy(exposeProxy = true, proxyTargetClass = true)
@ServletComponentScan(basePackages = {"im.zhaojun.zfile.core.filter", "im.zhaojun.zfile.module.storage.filter"})
@ComponentScan(basePackages = "im.zhaojun.zfile.*")
public class ZfileApplication {

    public static void main(String[] args) {
        SpringApplication.run(ZfileApplication.class, args);
    }

}