from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询文件目录'] = Template(
    '''问题背景：开发人员希望了解各个文件和目录在项目中的具体作用。\n\n
    1. 项目目录结构分析：项目的目录结构如下：${directory_structure}\n\n
    2. 主要文件和目录作用分析：
       - 列出每个关键文件和目录的作用及其与其他模块或组件的关系。
       - 示例：
         - ${file1}: 该文件负责${file1_purpose}，主要用于${file1_usage}。
         - ${directory1}: 该目录包含${directory1_content}，主要用于${directory1_usage}。\n\n
    3. 关联模块或组件：描述各个文件或目录与项目其他模块或组件的关联方式及其依赖关系。\n\n
    4. 文档参考（如README、设计文档等）：${documents}\n\n
    5. 根据以上分析步骤，生成关于项目文件和目录结构的详细报告，着重描述各个文件和目录的作用、用途及其在项目中的关系。

    '''
)
