import json

from llm_access import ask_llm
from preprocess.intention_recognition import get_intention
from prompt_template import prompt_template_base


def query1():
    query: str = '这个项目的架构是什么样的？'
    intention = get_intention(query)

    with open('resources/ref.json', 'r', encoding='utf-8') as ref_file:
        ref = json.load(ref_file)

    prompt = prompt_template_base[intention].substitute(ref)
    response = ask_llm(prompt)

    with open('resources/prompt.txt', 'w', encoding='utf-8') as prompt_file:
        prompt_file.write(prompt)

    with open('resources/response.md', 'w', encoding='utf-8') as output_file:
        output_file.write(response)


def query2():
    query: str = 'what’s the architecture of this repository?'
    intention = get_intention(query)

    with open('resources/reference.md', 'r', encoding='utf-8') as ref_file:
        ref = ref_file.read()

    prompt = prompt_template_base[intention].substitute(query=query, resources=ref)
    response = ask_llm(prompt)

    with open('resources/prompt.txt', 'w', encoding='utf-8') as prompt_file:
        prompt_file.write(prompt)

    with open('resources/response.md', 'w', encoding='utf-8') as output_file:
        output_file.write(response)


if __name__ == "__main__":
    query2()
