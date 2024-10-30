from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询功能'] = Template(
    '''问题背景：开发人员需要找到实现特定功能的代码位置，并了解其实现细节。\n\n
    1. 功能描述：该功能的描述为：${feature_description}\n\n
    2. 代码位置定位：
       - 项目中实现此功能的代码文件和位置如下：${code_location}
       - 具体文件路径和代码位置（如方法、类等）：${specific_path}
    
    3. 代码实现细节分析：
       - 代码中主要模块和方法的功能：${main_methods}
       - 关键逻辑的解释：${logic_explanation}
       - 此功能与其他模块的交互关系：${interactions_with_other_modules}
    
    4. 参考文档（如设计文档、API 文档等）：${documents}\n\n
    5. 根据以上分析步骤，生成关于该功能代码位置及实现细节的报告，包含文件路径、主要逻辑以及模块间的交互情况。

    '''
)
