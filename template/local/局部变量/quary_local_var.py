from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询局部变量'] = Template(
    '''问题背景：开发人员需要分析在文件 ${file_name} 中某个局部变量的作用。\n\n
    1. 局部变量的定义：
       - 变量名称：${local_variable_name}
       - 定义位置（方法或代码块）：${definition_location}\n\n
    2. 变量的功能描述：
       - 该变量的主要功能：${variable_function}
       - 在程序逻辑中的具体作用（如控制流程、存储计算结果等）：${variable_role}\n\n
    3. 变量的使用场景：
       - 变量在项目中的使用位置：${usage_locations}
       - 使用该变量的具体场景或案例：${usage_examples}\n\n
    4. 变量的影响：
       - 该变量对程序执行结果的影响：${impact_on_execution}
       - 修改该变量可能带来的后果：${consequences_of_modification}\n\n
    5. 参考文档：${documents}\n\n
    6. 根据以上分析步骤，生成关于局部变量作用的详细报告，包括定义、功能描述、使用场景及影响。

    '''
)
