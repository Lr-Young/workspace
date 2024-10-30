from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询功能'] = Template(
    '''问题背景：开发人员需要找到实现特定功能的代码位置，并了解其实现细节。\n\n
    1. 确定特定功能的名称，功能名称为：${feature_name}。\n\n
    2. 搜索项目中的函数定义，列出与该功能相关的函数及其定义位置。\n\n
    3. 分析相关函数的输入参数及返回值。\n\n
    4. 分析该函数的依赖关系，涉及的依赖模块和库如下：${dependencies}。\n\n
    5. 识别该功能的使用场景，包括该功能在项目中的使用位置和示例。\n\n
    6. 总结：根据以上分析步骤，生成关于该功能实现的详细报告，包括代码位置、实现细节及使用情况。\n
    '''
)


