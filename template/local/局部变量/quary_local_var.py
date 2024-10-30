from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['分析局部变量'] = Template(
    '''问题背景：开发人员需要分析在文件中某个局部变量的作用\n\n
    1. 查找该局部变量的出现位置，出现文件为：${file_name}\n\n
    2. 确定要分析的局部变量名称，变量名称为：${variable_name}\n\n
    3. 分析该局部变量的使用场景，包括使用次数和上下文，查找该变量在文件中的所有引用位置：\n
    4. 评估该局部变量对代码逻辑的影响，包括其在算法或功能中的作用。\n\n
    5. 总结：根据以上分析步骤，生成关于该局部变量的详细报告，包括其定义、使用情况和影响
    '''
)

