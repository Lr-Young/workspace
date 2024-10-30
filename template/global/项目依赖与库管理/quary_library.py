from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询第三方库'] = Template(
    '''问题背景：这是一个Java项目的代码仓库，开发人员需要了解项目中引入的第三方库及其功能\n\n
    1. 列出项目中引入的所有第三方库，项目依赖库包括：${dependencies}\n\n
    2. 分析每个第三方库的功能及用途。\n\n
    3. 确定每个第三方库的版本信息，版本信息如下：${version_info}\n\n
    4. 查阅第三方库的相关文档和资源，了解每个库的使用方式和最佳实践。\n\n
    5. 总结：根据以上分析步骤，生成关于项目中引入的第三方库的详细报告
    '''
)

example_answer = '''
项目中引入的第三方库及其功能、版本信息和使用方式总结如下：


项目中引入的第三方库:
Spring Boot
MyBatis
Lombok
Springfox
H2 Database
Logback


第三方库的功能及用途:
Spring Boot
功能: 提供了基于Spring框架的快速开发环境，简化了配置和部署。
用途: 用于构建和运行Spring应用程序。

MyBatis
功能: 支持自定义SQL、存储过程和高级映射的持久层框架。
用途: 用于数据库访问和ORM（对象关系映射）。

Lombok
功能: 通过注解简化Java代码，减少样板代码。
用途: 用于自动生成getter、setter、构造函数等。

Springfox
功能: 集成Swagger生成API文档。
用途: 用于生成和展示RESTful API文档。

H2 Database
功能: 嵌入式数据库，支持内存模式和持久化模式。
用途: 用于开发和测试环境中的数据库操作。

Logback
功能: 高效的日志框架，提供了丰富的日志配置和管理功能。
用途: 用于记录和管理应用程序日志。


第三方库的版本信息
版本信息可以在项目的pom.xml文件中找到。以下是部分库的版本信息：
Spring Boot: 版本信息在<spring-boot.version>标签中。
MyBatis: 版本信息在<mybatis.version>标签中。
Lombok: 版本信息在<lombok.version>标签中。
Springfox: 版本信息在<springfox.version>标签中。
H2 Database: 版本信息在<h2.version>标签中。
Logback: 版本信息在<logback.version>标签中。


第三方库的使用方式和最佳实践
Spring Boot
使用方式: 通过注解和自动配置简化Spring应用的开发。
最佳实践: 遵循Spring Boot官方文档中的配置和开发指南。

MyBatis
使用方式: 配置XML映射文件或注解方式定义SQL语句。
最佳实践: 使用MyBatis Generator自动生成代码，遵循官方文档中的最佳实践。

Lombok
使用方式: 在类上添加注解，如@Getter、@Setter、@Builder等。
最佳实践: 了解Lombok注解的作用和限制，避免滥用。

Springfox
使用方式: 通过注解和配置生成Swagger文档。
最佳实践: 遵循Springfox官方文档中的配置指南，确保API文档的准确性。

H2 Database
使用方式: 配置数据源，使用JDBC或JPA进行数据库操作。
最佳实践: 在开发和测试环境中使用H2，生产环境中使用其他数据库。

Logback
使用方式: 配置logback-spring.xml文件，定义日志级别和输出格式。
最佳实践: 根据应用需求配置日志级别，避免过多日志输出影响性能。


总结:
根据以上分析，项目中引入的第三方库主要用于简化开发、数据库操作、日志管理和API文档生成。
每个库都有其特定的功能和用途，版本信息可以在pom.xml文件中找到。
通过查阅相关文档和资源，可以了解每个库的使用方式和最佳实践，从而更好地应用于项目开发中。

'''


