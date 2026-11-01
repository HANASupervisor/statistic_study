
import json
from datetime import datetime
from zoneinfo import ZoneInfo


# ============================================
# 1. 실제 실행할 Tool 정의
# ============================================

def calculator(
    a: float,
    b: float,
    operation: str
) -> float:
    """
    Input:
        a: float
        b: float
        operation: str

    Output:
        float 또는 int
    """
    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return a / b

    else:
        raise ValueError("지원하지 않는 연산입니다.")


def get_weather(city: str) -> dict:
    """
    교육용 가상 날씨 데이터
    실제 날씨 API를 호출하지 않음
    """
    data = {
        "서울": {"weather": "맑음", "temp": 18},
        "부산": {"weather": "흐림", "temp": 21}
    }

    if city not in data:
        return {
            "city": city,
            "error": "날씨 정보가 없습니다."
        }

    return {
        "city": city,
        **data[city]
    }


def get_current_time() -> str:
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    return now.strftime("%Y-%m-%d %H:%M:%S")


# ============================================
# 2. Tool Registry
# ============================================

TOOL_REGISTRY = {
    "calculator": calculator,
    "get_weather": get_weather,
    "get_current_time": get_current_time
}


# ============================================
# 3. Decision: Tool 선택
# ============================================

def select_tool(question: str) -> dict | None:

    if "날씨" in question:
        city = next(
            (c for c in ("서울", "부산") if c in question),
            None
        )

        if city is None:
            return None

        return {
            "name": "get_weather",
            "arguments": {"city": city}
        }

    elif "계산" in question:
        # 강사 실습과 동일한 고정 인자
        return {
            "name": "calculator",
            "arguments": {
                "a": 10,
                "b": 5,
                "operation": "+"
            }
        }

    elif "시간" in question:
        return {
            "name": "get_current_time",
            "arguments": {}
        }

    return None


# ============================================
# 4. Action: Tool 실행
# ============================================

def execute_tool(decision: dict):
    """
    Input:
        {
            "name": "calculator",
            "arguments": {
                "a": 10,
                "b": 5,
                "operation": "+"
            }
        }

    Output:
        실행된 함수의 반환값
    """

    name = decision["name"]
    arguments = decision["arguments"]

    if name not in TOOL_REGISTRY:
        raise ValueError("등록되지 않은 Tool입니다.")

    tool_function = TOOL_REGISTRY[name]

    result = tool_function(**arguments)

    return result


# ============================================
# 5. Observation: 실행 결과 정리
# ============================================

def observation_step(result) -> dict:

    if isinstance(result, dict):
        return result

    return {"result": result}


# ============================================
# 6. Final Answer: 최종 답변 생성
# ============================================

def create_answer(
    tool_name: str,
    observation: dict
) -> str:

    if "error" in observation:
        return "Tool 실행 오류: " + observation["error"]

    if tool_name == "get_weather":
        return (
            f"{observation['city']}의 날씨는 "
            f"{observation['weather']}이고 "
            f"기온은 {observation['temp']}°C입니다."
        )

    elif tool_name == "calculator":
        return f"계산 결과는 {observation['result']}입니다."

    elif tool_name == "get_current_time":
        return f"현재 시간은 {observation['result']}입니다."

    return str(observation)


# ============================================
# 7. 전체 Agent 실행
# ============================================

def run_agent(question: str) -> str | None:

    print("\n[User Question]", question)

    # STEP 1. Tool 선택
    decision = select_tool(question)

    if decision is None:
        print("사용할 Tool이 없습니다.")
        return None

    print(
        "[Decision]",
        json.dumps(decision, ensure_ascii=False)
    )

    # STEP 2. Tool 실행
    try:
        result = execute_tool(decision)
    except (ValueError, TypeError, KeyError) as e:
        result = {"error": str(e)}

    print("[Action]", decision["name"])

    # STEP 3. Observation
    observation = observation_step(result)

    print(
        "[Observation]",
        json.dumps(observation, ensure_ascii=False)
    )

    # STEP 4. Final Answer
    answer = create_answer(
        decision["name"],
        observation
    )

    print("[Final Answer]", answer)

    return answer


# ============================================
# 8. 테스트
# ============================================

if __name__ == "__main__":

    run_agent("서울 날씨 알려줘")
    run_agent("계산해주세요")
    run_agent("현재 시간 알려줘")
    run_agent("안녕하세요")
