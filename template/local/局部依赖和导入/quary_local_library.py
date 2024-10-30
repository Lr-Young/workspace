from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询导入库'] = Template(
    '''问题背景：开发人员需要分析在文件 ${file_name} 中导入的模块或库的作用。\n\n
    1. 导入的模块或库列表：
       - 模块/库名称：${module_name}
       - 导入位置：${import_location}\n\n
    2. 每个模块/库的作用：
       - ${module_name}：
         - 主要功能：${module_functionality}
         - 提供的关键功能或服务：${key_features}\n\n
    3. 在项目中的使用场景：
       - 该模块/库在项目中的使用位置：${usage_locations}
       - 具体使用案例或功能实现：${usage_examples}\n\n
    4. 导入模块/库的依赖关系：
       - 依赖的其他模块/库：${dependencies}
       - 依赖关系对项目的影响：${dependency_impact}\n\n
    5. 参考文档（如官方文档、使用指南等）：${documents}\n\n
    6. 根据以上分析步骤，生成关于导入模块或库的作用的详细报告，包括功能、使用场景及依赖关系。

    '''
)
