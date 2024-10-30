from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询数据库'] = Template(
    '''问题背景：开发人员需要了解项目中数据库交互或网络请求的处理方式。\n\n
    1. 数据库交互处理：
       - 数据库类型和连接方式：项目使用的数据库为：${database_type}，通过 ${connection_method} 进行连接。
       - 数据库交互模块：${db_modules}
       - 关键方法或类：${db_methods}
       - 主要SQL查询或ORM操作：${db_operations}\n\n
    2. 网络请求处理：
       - 网络请求库和协议：项目中用于网络请求的库或框架为：${network_library}，使用的协议包括：${protocols}
       - 网络请求的模块和类：${network_modules}
       - 关键方法或接口：${network_methods}
       - 错误处理和重试机制：${error_handling}\n\n
    3. 配置项：
       - 数据库和网络请求的主要配置项：${config_items}
       - 示例配置及其作用：
         - ${example_config1}: 用于${config1_usage}
         - ${example_config2}: 用于${config2_usage}\n\n
    4. 参考文档（如数据库手册、API 文档等）：${documents}\n\n
    5. 根据以上分析步骤，生成关于项目数据库交互的详细报告，包含使用的库、关键模块、方法和配置说明。

    '''
)
