from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询函数'] = Template(
    '''问题背景：开发人员需要找到某个特定函数的具体实现位置，并了解其输入和输出\n\n
    1. 确定要查找的特定函数名称，函数名称为：${function_name}\n\n
    2. 根据名称查找该函数的具体实现位置。\n\n
    3. 分析该函数的输入参数及其类型。\n\n
    4. 分析该函数的输出结果及其类型。\n\n
    5. 总结：根据以上分析步骤，生成关于该函数的详细报告，包括其实现位置、输入和输出信息
    '''
)

