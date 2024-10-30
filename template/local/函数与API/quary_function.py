from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询函数'] = Template(
    '''问题背景：开发人员需要找到某个特定函数的具体实现位置，并了解其输入和输出。\n\n
    1. 函数定义和实现位置：
       - 函数名称：${function_name}
       - 实现位置（文件名及路径）：${implementation_location}\n\n
    2. 函数的输入参数：
       - 输入参数列表及类型：
         - ${input_param1}: 类型为 ${input_type1}，用于${input_usage1}
         - ${input_param2}: 类型为 ${input_type2}，用于${input_usage2}\n\n
    3. 函数的返回值：
       - 返回值类型和含义：
         - 返回类型：${return_type}
         - 返回值描述：${return_description}\n\n
    4. 函数的调用位置和用途：
       - 函数被调用的位置或模块：${usage_locations}
       - 函数的用途或场景：${usage_scenarios}\n\n
    5. 示例调用（如适用）：
       - 示例调用代码：${example_usage}\n\n
    6. 参考文档（如函数说明、API文档等）：${documents}\n\n
    7. 根据以上分析步骤，生成关于该函数的详细说明报告，包括其定义位置、输入输出参数及调用用途。

    '''
)
