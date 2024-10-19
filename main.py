from openai import OpenAI


API_KEY = '	sk-3359785840be415f8b75da9a52b713a3'  # 通义千问API lry


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


print(ask_llm("what’s the architecture of this repository ?"))
