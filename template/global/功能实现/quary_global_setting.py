from string import Template

prompt_template_base: dict[str, Template] = dict()

prompt_template_base['查询全局配置'] = Template(
    '''问题背景：开发人员需要了解某个全局配置文件的作用，并了解如何通过修改它来调整项目的行为。\n\n
    1. 配置文件概述：该全局配置文件为：${config_file}\n
       - 文件路径：${file_path}
       - 主要作用：${file_purpose}
       - 典型配置项：${key_settings}\n\n
    2. 配置项详解及其作用：
       - 配置项分析：${setting_details}
       - 示例配置及用途说明：
         - ${example_setting1}: 用于${setting1_usage}
         - ${example_setting2}: 用于${setting2_usage}\n\n
    3. 修改配置以改变项目行为：
       - 描述如何调整配置项来实现不同的项目行为。
       - 例如：${example_setting_modification1} 会导致 ${behavior_change1}
       - 例如：${example_setting_modification2} 会导致 ${behavior_change2}\n\n
    4. 参考文档（如项目手册、配置说明等）：${documents}\n\n
    5. 根据以上分析步骤，生成关于该全局配置文件的详细说明，包括其作用、关键配置项及其对项目行为的影响。

    '''
)
