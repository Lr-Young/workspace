from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询数据库'] = Template(
    '''问题背景：开发人员需要了解项目中与数据库交互的处理方式。\n\n
    1. 确定使用的数据库类型。\n\n
    2. 列出与数据库交互的主要模块或类。\n\n
    3. 分析数据库交互的方式，主要使用的方式（如ORM、JDBC等）。\n\n
    4. 识别数据库连接的配置，数据库连接配置文件和相关参数如下：${connection_config}。\n\n
    5. 分析数据访问层的设计模式（如DAO、Repository等），所用设计模式为：${design_pattern}。\n\n
    6. 总结：根据以上分析步骤，生成关于项目中数据库交互处理方式的详细报告，包括使用的数据库、交互方式及操作示例。\n
    '''
)

