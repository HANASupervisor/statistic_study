import json
import requests

MODEL = "llama3.2"
OLLAMA_URL = "http://localhost:11434/api/chat"

tools = [
    {
        "name": "get_weather",
        "description": "도시의 날씨를 조회합니다.",
        "parameters": {"location": "도시명"}
    },
    {
        "name": "calculator",
        "description": "계산식을 계산합니다.",
        "parameters": {"expression": "수학 계산식"}
    }
]


def select_tool(question: str) -> dict | None:

    # STEP 1. LLM에게 전달할 System Prompt
    system_prompt = f"""
    당신은 Tool Selection AI입니다.

    사용할 수 있는 도구:
    {json.dumps(tools, ensure_ascii=False)}

    사용자 질문을 보고 적절한 도구 하나를 선택하세요.

    반드시 다음 JSON 형식만 출력하세요.

    {{
        "name": "도구 이름",
        "arguments": {{
            "인자명": "인자값"
        }}
    }}

    사용할 도구가 없다면 null을 출력하세요.
    """

    # STEP 2. Ollama Chat API 요청
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False,
        "format": "json"
    }

    # STEP 3. POST 요청
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    # STEP 4. HTTP 상태 확인
    response.raise_for_status()

    # STEP 5. JSON 응답에서 LLM 메시지 추출
    result = response.json()
    content = result["message"]["content"]

    # STEP 6. JSON 문자열을 Python dict로 변환
    decision = json.loads(content)

    if decision == {} or decision is None:
        return None
    # 선택 된 툴이름과 arguements를 반환
    return decision # Decision: {'name': 'calculator', 'arguments': {'expression': '10 + 20'}}


# ============================================
# 2. Calculator 도구 정의
# ============================================
import ast
import operator

# 허용할 수학 연산자
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def calculator(expression: str):
    """
    INPUT:
        expression = "10 + 20"

    OUTPUT:
        30
    """

    # 문자열을 Python 수식 구문 트리(AST)로 변환
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value

        if isinstance(node, ast.BinOp):
            op = OPERATORS.get(type(node.op))

            if op is not None:
                left = evaluate(node.left)
                right = evaluate(node.right)
                return op(left, right)

        if isinstance(node, ast.UnaryOp):
            value = evaluate(node.operand)

            if isinstance(node.op, ast.USub):
                return -value
            if isinstance(node.op, ast.UAdd):
                return value

        raise ValueError("지원하지 않는 계산식입니다.")

    return evaluate(tree)


# ============================================
# 3. Tool Execution
# ============================================
def execute_tool(decision: dict):
    """
    INPUT:
        {
            "name": "calculator",
            "arguments": {
                "expression": "10 + 20"
            }
        }

    OUTPUT:
        30
    """

    # LLM이 선택한 도구 이름
    tool_name = decision["name"]

    # LLM이 생성한 도구 인자
    arguments = decision["arguments"]

    # calculator 도구라면 실제 함수 실행
    if tool_name == "calculator":
        return calculator(arguments["expression"])

    # 아직 날씨 도구는 구현하지 않음
    raise ValueError(f"지원하지 않는 도구: {tool_name}")


# ============================================
# 4. 전체 실행
# ============================================
if __name__ == "__main__":

    question = "10 + 20을 계산해줘."

    # STEP 1. 어떤 도구를 사용할지 선택
    decision = select_tool(question)

    print("Decision:", decision)

    # STEP 2. 선택한 도구 실행
    if decision is not None:
        result = execute_tool(decision)

        # STEP 3. 실행 결과 확인
        print("Observation:", result)
    else:
        print("사용할 도구가 없습니다.")