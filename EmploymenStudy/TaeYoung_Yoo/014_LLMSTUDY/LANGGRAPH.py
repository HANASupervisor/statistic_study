from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# ============================================
# 1. State 데이터 구조 정의
# ============================================
class AgentState(TypedDict):
    question: str
    context: str
    answer: str


# ============================================
# 2. Input Node
# ============================================
def input_node(state: AgentState) -> dict:

    # STEP 1. 질문 가져오기
    question = state["question"]

    # STEP 2. 입력 질문 출력
    print("[Input Node]")
    print("질문:", question)

    # STEP 3. State 변경 없이 반환
    return {}


# ============================================
# 3. Process Node
# ============================================
def process_node(state: AgentState) -> dict[str, str]:

    # STEP 1. 현재 State에서 질문 가져오기
    question = state["question"]

    # STEP 2. 질문 처리 결과 생성
    context = f"분석된 질문: {question}"

    # STEP 3. context 필드 갱신
    return {
        "context": context
    }


# ============================================
# 4. Answer Node
# ============================================
def answer_node(state: AgentState) -> dict[str, str]:

    # STEP 1. 이전 Node에서 생성한 Context 가져오기
    context = state["context"]

    # STEP 2. 답변 문자열 생성
    answer = f"{context} / 처리 완료"

    # STEP 3. answer 필드 갱신
    return {
        "answer": answer
    }


# ============================================
# 5. LangGraph 구성
# ============================================
def build_graph():

    # STEP 1. AgentState 기반 StateGraph 생성
    builder = StateGraph(AgentState)

    # STEP 2. Node 등록
    builder.add_node("input", input_node)
    builder.add_node("process", process_node)
    builder.add_node("answer", answer_node)

    # STEP 3. Edge 연결
    builder.add_edge(START, "input")
    builder.add_edge("input", "process")
    builder.add_edge("process", "answer")
    builder.add_edge("answer", END)

    # STEP 4. 그래프 컴파일 후 반환
    return builder.compile()


# ============================================
# 6. 메인 프로그램
# ============================================
if __name__ == "__main__":

    # STEP 1. 그래프 생성
    graph = build_graph()

    # STEP 2. 초기 State 정의
    initial_state: AgentState = {
        "question": "회사의 휴가 규정은?",
        "context": "",
        "answer": ""
    }

    # STEP 3. 그래프 실행
    final_state = graph.invoke(initial_state)

    # STEP 4. 최종 State 출력
    print("\n[최종 State]")
    print(final_state)

    # STEP 5. 검증
    assert final_state["question"] == "회사의 휴가 규정은?"
    assert final_state["context"] == "분석된 질문: 회사의 휴가 규정은?"
    assert final_state["answer"].endswith("처리 완료")

    print("\n모든 검증 통과!")