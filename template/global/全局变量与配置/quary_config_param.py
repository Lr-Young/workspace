from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询配置参数'] = Template(
    '''问题背景：开发人员需要了解在全局配置中的参数是如何定义和使用的。\n\n
    1. 确定全局配置文件的名称及路径，配置文件名称为：${config_file_name}，路径为：${config_file_path}。\n\n
    2. 列出配置文件中的关键参数，包括关键参数及其默认值。\n\n
    3. 分析参数的定义方式，描述参数在配置文件中的定义格式及语法。\n\n
    4. 理解参数的使用场景，列出在代码中如何引用和使用这些参数的示例。\n\n
    5. 识别参数的依赖关系，分析这些参数在项目中的依赖情况及对其他模块的影响。\n\n
    6. 提供参数修改的影响，讨论修改这些参数对项目行为的潜在影响。\n\n
    7. 阅读参考文档（如官方文档、使用指南等）：${documents}。\n\n
    8. 总结：根据以上分析步骤，生成关于全局配置参数定义和使用的详细报告，包括参数的定义、使用场景及影响。\n
    '''
)

