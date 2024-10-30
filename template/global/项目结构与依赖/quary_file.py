from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询文件目录'] = Template(
    '''问题背景：这是一个Java项目的代码仓库，开发人员希望了解各个文件和目录在项目中的具体作用。\n\n
    1. 列出项目的主要目录结构，项目目录结构如下：${directory_structure}。\n\n
    2. 分析每个主要目录的作用，描述每个目录在项目中的功能和用途}。\n\n
    3. 识别关键文件，列出项目中的关键文件及其作用。\n\n
    4. 讨论文件之间的关系，说明各个文件如何相互协作。\n\n
    5. 识别文件和目录的依赖，其中文件和目录之间的依赖关系为：${file_dependencies}。\n\n
    6. 提供文件使用示例，展示某个文件在项目中的实际使用情况。\n\n
    7. 总结：根据以上分析步骤，生成关于项目中各个文件和目录具体作用的详细报告，包括目录结构、关键文件及其功能。\n
    '''
)

