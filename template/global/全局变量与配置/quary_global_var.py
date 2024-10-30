from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询全局变量'] = Template(
    '''问题背景：开发人员需要了解项目中的全局变量或常量如何影响代码的运行。\n\n
    1. 全局变量和常量的定义：
       - 定义全局变量和常量的文件或类：${global_definitions_location}
       - 示例变量和常量：
         - ${global_variable1}: 用于${global_variable1_usage}
         - ${constant1}: 用于${constant1_usage}\n\n
    2. 全局变量和常量的作用范围及生命周期：
       - 变量或常量的作用域（如全局作用域、模块作用域）：${scope}
       - 生命周期（如初始化时机、释放或销毁时间）：${lifecycle}\n\n
    3. 全局变量和常量对代码运行的影响：
       - 在项目中被引用的位置或模块：${usage_locations}
       - 对代码行为的具体影响（如控制程序流程、参数传递）：${runtime_impact}
       - 修改这些变量或常量时可能带来的变化：${modification_impact}\n\n
    4. 常量的管理和更新策略：
       - 常量的更新策略（如环境变量、配置文件更新）：${update_strategy}
       - 变量和常量的可维护性和可扩展性建议：${maintainability_recommendations}\n\n
    5. 参考文档（如变量使用指南、代码规范文档等）：${documents}\n\n
    6. 根据以上分析步骤，生成关于项目全局变量或常量的影响的详细报告，包括变量和常量的定义、使用方式及对项目行为的影响。

    '''
)
