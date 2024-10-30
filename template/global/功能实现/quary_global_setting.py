from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询全局配置'] = Template(
    '''问题背景：开发人员需要了解某个全局配置文件的作用，并了解如何通过修改它来调整项目的行为。\n\n
    1. 确定全局配置文件的名称及路径，配置文件名称为：${config_file_name}，路径为：${config_file_path}。\n\n
    2. 分析配置文件的主要内容，包括配置文件的关键参数及其默认值。\n\n
    3. 理解配置文件的作用，描述该配置文件对项目运行的影响及其目的。\n\n
    4. 识别可修改的参数及其影响，列出可以调整的参数及其对项目行为的影响。\n\n
    5. 阅读相关参考文档（如官方文档、使用指南等）：${documents}。\n\n
    6. 总结：根据以上分析步骤，生成关于全局配置文件作用及修改方法的详细报告，包括文件内容、作用及调整方法。\n
    '''
)

