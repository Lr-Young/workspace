from openai import OpenAI

API_KEY = 'sk-3359785840be415f8b75da9a52b713a3'  # 通义千问API key


def ask_llm(prompt: str, system_prompt: str = 'you are a helpful assistant') -> str:
    try:
        client = OpenAI(
            api_key=API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"LLM调用错误：{e}"


def build_prompt(_query, _plan, _reference):
    return f"""Here are some relevant code fragments from files of a repo:
{_reference}
Please answer the question according to above code fragments:
{_query}
You can answer the question by following the steps below:
{_plan}   
"""


if __name__ == "__main__":
    query = "what’s the architecture of this repository?"

    plan = """
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
"""

    with open('reference.md', encoding='utf8') as f:
        reference = f.read()

    print(ask_llm(build_prompt(query, plan, reference)))
