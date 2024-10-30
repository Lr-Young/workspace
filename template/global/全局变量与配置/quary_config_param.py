from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询配置参数'] = Template(
    '''问题背景：开发人员需要了解全局配置参数是如何定义和使用的。\n\n
    1. 全局配置参数的定义方式：
       - 配置参数定义文件位置：${config_file_location}
       - 主要配置文件的格式（如 `properties`、`yaml`、`xml` 等）：${config_file_format}
       - 示例配置参数：
         - ${param1}: 用于${param1_usage}
         - ${param2}: 用于${param2_usage}\n\n
    2. 全局配置参数的加载和初始化：
       - 加载配置的模块或方法：${load_module_or_method}
       - 配置初始化的时机和顺序：${initialization_timing}
       - 参数的默认值及其处理方式：${default_value_handling}\n\n
    3. 全局配置参数的使用方式：
       - 配置参数在项目中被引用的位置或模块：${usage_locations}
       - 具体使用场景（如控制某些功能、启用日志记录等）：${usage_scenarios}
       - 修改配置参数对项目行为的影响：${modification_impact}\n\n
    4. 配置管理和安全性：
       - 配置管理策略（如版本控制、环境变量）：${config_management_strategy}
       - 安全性措施（如敏感参数加密、环境隔离）：${security_measures}\n\n
    5. 参考文档（如配置手册、API 文档等）：${documents}\n\n
    6. 根据以上分析步骤，生成关于项目全局配置参数的详细报告，包括参数定义、加载方式、使用场景及管理策略。

    '''
)
