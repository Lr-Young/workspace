from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询核心模块'] = Template(
    '''问题背景：开发人员希望深入了解项目的核心模块。\n\n
    1. 识别出项目的主要核心模块。\n\n
    2. 分析每个核心模块的功能，描述每个模块的具体功能和职责。\n\n
    3. 理解模块间的交互，说明各个核心模块之间的交互关系。\n\n
    4. 识别模块的依赖关系，其中模块之间的依赖关系为：${module_dependencies}。\n\n
    5. 阅读相关参考文档（如设计文档、API文档等）：${documents}。\n\n
    6. 总结：根据以上分析步骤，生成关于项目核心模块的详细报告，包括模块功能、交互和实现细节。\n
    '''
)

