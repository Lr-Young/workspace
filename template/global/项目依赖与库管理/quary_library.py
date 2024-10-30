from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询第三方库'] = Template(
    '''问题背景：开发人员需要了解项目中引入的第三方库及其功能。\n\n
    1. 第三方库列表和功能说明：
       - 项目中引入的第三方库如下：
         - ${library1}: 主要功能是${library1_purpose}
         - ${library2}: 主要功能是${library2_purpose}
         - ${library3}: 主要功能是${library3_purpose}\n\n
    2. 库的版本信息和兼容性：
       - ${library1} 版本：${library1_version}，兼容性说明：${library1_compatibility}
       - ${library2} 版本：${library2_version}，兼容性说明：${library2_compatibility}\n\n
    3. 库的配置及使用情况：
       - 配置项示例和用途：
         - ${config_item1}: 用于配置 ${library1} 的 ${config1_usage}
         - ${config_item2}: 用于配置 ${library2} 的 ${config2_usage}\n\n
    4. 依赖管理工具及配置文件：
       - 使用的依赖管理工具：${dependency_tool}
       - 相关配置文件（如 `pom.xml`、`build.gradle`）：${dependency_files}\n\n
    5. 参考文档（如库的官方文档、API 文档等）：${documents}\n\n
    6. 根据以上分析步骤，生成关于项目中引入的第三方库及其用途的详细报告，包含功能描述、版本信息、配置示例及兼容性说明。
    
    '''
)
