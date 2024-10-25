from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询核心模块'] = Template(
    '''这个项目的核心模块有哪些？
    '''
)

prompt_template_base['查询项目结构'] = Template(
    '''问题背景：这是一个Java项目的代码仓库，开发人员询问项目代码仓库的整体架构，主要关注其目录结构、模块职责、依赖关系方面\n\n
    1. 分析项目的目录结构，项目代码的目录结构如下：${directory_structure}\n\n
    2. 分析项目的主要模块及其作用，核心模块包括：${modules}\n\n
    3. 识别项目的依赖，项目的依赖包括：${dependencies}\n\n
    4. 阅读项目相关资料（如README、设计文档、API文档等）：${documents}\n\n
    5. 总结：根据以上分析步骤，生成关于这个代码仓库的详细架构分析报告
    
    注意：只需要输出最后的总结，中间分析步骤不需要输出
    ''')

prompt_template_base['query the architecture'] = Template(
    '''Here are some relevant code fragments from files of a repo:${resources}\n\n
    Please answer the question according to above code fragments:${query}\n\n
    You can answer the question by following the steps below:
    1. Overview of the Repository Structure: Begin by providing a high-level overview of the repository's structure. 
    2. Main Components Identification: Identify and describe the main components of the codebase. 
    3. Data Flow Analysis: Describe how data flows through the system. 
    4. Dependency Management: Discuss how dependencies are managed within the repository. 
    5. Build and Deployment Process: Outline the process for building and deploying the code. 
    6. Testing Strategy: Explain the testing strategy employed in the repository. 
    7. Configuration Management: Discuss how configuration is managed in the project. 
    8. Documentation: Review the documentation provided within the repository.
    9. Code Style and Standards: Comment on the code style and standards observed in the repository. 
    10. Security Features: Highlight any security features or practices implemented in the codebase. 
    11. Performance Considerations: Discuss any performance optimizations or considerations evident in the codebase. 
    '''
)