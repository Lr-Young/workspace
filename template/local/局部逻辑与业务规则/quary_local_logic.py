from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询代码段逻辑'] = Template(
    '''问题背景：开发人员需要分析在文件 ${file_name} 中选中的代码段的业务逻辑及实现原因。\n\n
    1. 代码段内容：
       - 选中的代码段：\n
       \`\`\`java\n
       ${code_snippet}\n
       \`\`\`\n\n
    2. 业务逻辑分析：
       - 该代码段实现的主要功能：${functionality}
       - 具体的业务流程和逻辑描述：${business_logic}\n\n
    3. 相关条件和影响：
       - 该代码段执行的前提条件和依赖关系：${preconditions}\n\n
    4. 参考文档（如设计文档、业务需求文档等）：${documents}\n\n
    5. 根据以上分析步骤，生成关于该代码段业务逻辑和实现原因的详细报告。

    '''
)

prompt_template_base['分析代码段'] = Template(
    '''问题背景：开发人员需要分析在文件中选中的代码段的业务逻辑及实现原因\n\n
    1. 确定要分析的代码段，代码段内容为：${code_snippet}\n\n
    2. 分析该代码段中使用的关键变量和函数。\n\n
    3. 解析该代码段的业务逻辑，包括主要功能和处理流程。\n\n
    4. 理解该代码段的实现原因，考虑设计选择、性能因素或其他考虑。\n\n
    5. 总结：根据以上分析步骤，生成关于该代码段的详细报告，包括其业务逻辑和实现原因
    '''
)

