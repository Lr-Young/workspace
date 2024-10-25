
def get_intention(query: str) -> str:
    # TODO 从用户查询中识别意图
    if query == 'what’s the architecture of this repository?':
        return 'query the architecture'
    return '查询项目结构'
