from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['分析导入模块'] = Template(
    '''问题背景：开发人员需要分析在文件中导入的模块或库的作用\n\n
    1. 找到在文件中导入的所有模块或库，导入的模块或库如下：${imported_modules}\n\n
    2. 分析每个导入模块或库的主要功能，包括第三方库的功能，模块的相关信息{modules_info}\n\n
    3. 识别模块或库的依赖关系，分析这些导入的模块或库与项目其他部分的依赖关系：${module_dependencies}。\n\n
    4. 确定这些模块或库在代码中的使用情况，分析使用到相关模块或库的代码上下文。\n\n
    5. 总结：根据以上分析步骤，生成关于导入模块或库的详细报告，包括其作用和影响
    '''
)

