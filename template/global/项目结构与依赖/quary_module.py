from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询核心模块'] = Template(
    '''问题背景：这是一个Java项目的代码仓库，开发人员希望深入了解项目的核心模块。\n\n
    1. 识别项目的核心模块并分析其功能，每个核心模块的功能如下：${core_modules}\n\n
    2. 分析核心模块的接口和交互：列出核心模块中暴露的主要接口及其与其他模块的交互方式\n\n
    3. 依赖分析：列出每个核心模块的依赖关系，包括外部依赖、第三方库或工具。\n\n
    4. 阅读项目相关资料（如README、设计文档、API文档等）：${documents}\n\n
    5. 根据以上分析步骤，生成关于项目核心模块的详细报告，包括每个模块的作用、接口、依赖等关键信息。
    '''
)

