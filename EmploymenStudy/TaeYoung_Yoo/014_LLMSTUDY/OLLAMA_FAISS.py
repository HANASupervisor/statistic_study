import numpy as np
import faiss
import requests

from sentence_transformers import SentenceTransformer
# 이코드는 그럼 모델로딩하고 
# 청크 임베딩하고 
# faiss생성하고 
# faiss안에 있는 정보검색해서 유사한거 찾아서 
# 그값 반환하는 코드

# ============================================
# 0. 환경 설정
# ============================================

EMBEDDING_MODEL = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"

NO_ANSWER = "제공된 문서에서 확인할 수 없습니다."


# ============================================
# 1. 문서 Chunking
# ============================================
def split_document(
    document: str,
    chunk_size: int = 150,
    overlap: int = 30
) -> list[str]:
    """
    Input:
        document: 원본 문자열
        chunk_size: Chunk 최대 글자 수
        overlap: 인접 Chunk 사이 중복 글자 수

    Output:
        list[str]: 분할된 Chunk 리스트
    """

    # STEP 1. Chunk 크기 및 Overlap 유효성 검증
    if chunk_size <= 0:
        raise ValueError("chunk_size는 0보다 커야 합니다.")

    if not 0 <= overlap < chunk_size:
        raise ValueError("overlap 범위가 잘못되었습니다.")

    # STEP 2. Chunk를 저장할 리스트와 시작 위치 생성
    chunks = []
    start = 0

    # STEP 3. 원본 문서를 끝까지 순회
    while start < len(document):

        # STEP 4. Chunk의 끝 위치 계산
        end = min(start + chunk_size, len(document))

        # STEP 5. start부터 end까지 문자열 추출
        chunk = document[start:end]
        chunks.append(chunk)

        # STEP 6. 마지막 Chunk라면 반복 종료
        if end == len(document):
            break

        # STEP 7. Overlap을 적용하여 다음 시작 위치 이동
        start += chunk_size - overlap

    return chunks


# ============================================
# 2. Embedding Model 로딩
# ============================================
def load_model() -> SentenceTransformer:

    # STEP 1. 문장을 벡터로 변환할 모델 로드
    model = SentenceTransformer(EMBEDDING_MODEL)

    return model


# ============================================
# 3. Chunk Embedding
# ============================================
def create_embeddings(
    model: SentenceTransformer,
    chunks: list[str]
) -> np.ndarray:
    """
    Input:
        model: SentenceTransformer 모델
        chunks: list[str]

    Output:
        vectors: np.ndarray (N, 384)
    """

    # STEP 1. Chunk들을 임베딩 벡터로 변환
    vectors = model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # STEP 2. FAISS에서 사용할 float32 형식으로 변환
    vectors = np.asarray(
        vectors,
        dtype=np.float32
    )

    return vectors


# ============================================
# 4. FAISS Index 생성
# ============================================
def build_faiss_index(
    vectors: np.ndarray
) -> faiss.Index:

    # STEP 1. 임베딩 벡터의 차원 확인
    dimension = vectors.shape[1]

    # STEP 2. 코사인 유사도 검색을 위한 IP Index 생성
    # 문서와 질문 모두 정규화해야 함
    index = faiss.IndexFlatIP(dimension)

    # STEP 3. Index에 임베딩 벡터 저장
    index.add(vectors)

    return index


# ============================================
# 5. Retrieval
# ============================================
def retrieve_chunks(
    query: str,
    model: SentenceTransformer,
    index: faiss.Index,
    chunks: list[str],
    top_k: int = 3
) -> list[dict]:
    """
    Input:
        query: str
        model: SentenceTransformer
        index: FAISS Index
        chunks: list[str]
        top_k: int

    Output:
        list[dict]
        [
            {
                "rank": 1,
                "chunk_id": 2,
                "score": 0.85,
                "text": "..."
            }
        ]
    """

    # STEP 1. Top-K 유효성 검증
    if top_k < 1:
        raise ValueError("top_k는 1 이상이어야 합니다.")

    # STEP 2. 저장된 문서가 없다면 빈 리스트 반환
    if index.ntotal == 0:
        return []

    # STEP 3. 사용자 질문을 임베딩 벡터로 변환
    query_vector = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # STEP 4. FAISS 검색용 float32로 변환
    query_vector = np.asarray(
        query_vector,
        dtype=np.float32
    )

    # STEP 5. 검색할 문서 개수를 실제 저장 개수로 제한
    k = min(top_k, index.ntotal)

    # STEP 6. FAISS에서 유사한 Chunk 검색
    scores, indices = index.search(
        query_vector,
        k
    )

    # STEP 7. 검색 결과 저장용 리스트 생성
    results = []

    # STEP 8. 검색 순위, 문서 인덱스, 점수 연결
    for rank, (idx, score) in enumerate(
        zip(indices[0], scores[0]),
        start=1
    ):
        if idx < 0:
            continue

        # STEP 9. 검색 결과를 딕셔너리로 저장
        results.append({
            "rank": rank,
            "chunk_id": int(idx),
            "score": float(score),
            "text": chunks[int(idx)]
        })

    return results


# ============================================
# 6. Context Builder
# ============================================
def build_context(
    results: list[dict]
) -> str:
    """
    Input:
        list[dict]: Retrieval 결과

    Output:
        str: LLM에 전달할 Context
    """

    # STEP 1. 검색 결과가 없으면 빈 문자열 반환
    if not results:
        return ""

    # STEP 2. 각 검색 결과에서 원본 텍스트 추출
    context_parts = []

    for i, item in enumerate(results, start=1):

        context_parts.append(
            f"[문서 {i}]\n{item['text']}"
        )

    # STEP 3. 여러 문서를 빈 줄로 연결
    context = "\n\n".join(context_parts)

    return context


# ============================================
# 7. Prompt Builder
# ============================================
def build_prompt(
    question: str,
    context: str
) -> str:

    # STEP 1. LLM에게 역할과 답변 규칙 전달
    # STEP 2. 검색된 Context와 사용자 질문 삽입
    prompt = f"""
    당신은 회사 내부 문서에 근거하여 답변하는 AI입니다.

    [답변 규칙]
    1. 제공된 Context의 정보만 사용하세요.
    2. Context에 없는 내용은 추측하지 마세요.
    3. 근거가 없다면 다음 문장으로 답하세요.
    "{NO_ANSWER}"

    [Context]
    {context}

    [Question]
    {question}

    [Answer]
    """

    return prompt


# ============================================
# 8. Ollama LLM 호출
# ============================================
def call_llm(prompt: str) -> str:

    # STEP 1. Ollama API로 전달할 JSON 구성
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    # STEP 2. Ollama 서버에 POST 요청
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    # STEP 3. HTTP 오류 확인
    response.raise_for_status()

    # STEP 4. JSON 응답을 딕셔너리로 변환
    result = response.json()

    # STEP 5. 생성된 답변 문자열 반환
    return result["response"]


# ============================================
# 9. 전체 RAG Pipeline
# ============================================
def rag_pipeline(
    question: str,
    model: SentenceTransformer,
    index: faiss.Index,
    chunks: list[str],
    top_k: int = 3,
    use_llm: bool = False
) -> dict:

    # STEP 1. 사용자 질문과 관련된 Chunk 검색
    results = retrieve_chunks(
        question,
        model,
        index,
        chunks,
        top_k
    )

    # STEP 2. 검색한 Chunk들을 Context로 결합
    context = build_context(results)

    # STEP 3. LLM에게 전달할 Prompt 생성
    prompt = build_prompt(question, context)

    # STEP 4. 선택적으로 Ollama 답변 생성
    if not results:
        answer = NO_ANSWER
    elif use_llm:
        answer = call_llm(prompt)
    else:
        answer = "(LLM 실행 생략)"

    # STEP 5. 전체 결과 반환
    return {
        "question": question,
        "retrieved_results": results,
        "context": context,
        "prompt": prompt,
        "answer": answer
    }


# ============================================
# 10. 메인 프로그램
# ============================================
if __name__ == "__main__":

    document = """
    제1조 휴가 신청
    직원은 사내 인사 시스템에서 휴가를 신청해야 합니다.

    제2조 휴가 승인
    3일 이상의 연속 휴가는 팀장의 승인이 필요합니다.

    제3조 출장비
    국내 출장비는 1일 5만원입니다.

    제4조 숙박비
    출장 숙박비는 1박당 최대 10만원입니다.

    제5조 복리후생
    회사는 식대와 교육비를 지원합니다.
    """

    # STEP 1. 문서를 Chunk로 분할
    chunks = split_document(
        document,
        chunk_size=100,
        overlap=20
    )

    # STEP 2. 임베딩 모델 로딩
    model = load_model()

    # STEP 3. Chunk Embedding
    vectors = create_embeddings(model, chunks)

    # STEP 4. FAISS Index 생성
    index = build_faiss_index(vectors)

    # STEP 5. 사용자 질문
    question = "출장 숙박비는 얼마까지 지원되나요?"

    # STEP 6. 전체 RAG 실행
    result = rag_pipeline(
        question,
        model,
        index,
        chunks,
        top_k=3,
        use_llm=True
    )

    print("\n=== Embedding Shape ===")
    print(vectors.shape)

    print("\n=== Retrieval ===")
    for item in result["retrieved_results"]:
        print(item)

    print("\n=== Context ===")
    print(result["context"])

    print("\n=== Prompt ===")
    print(result["prompt"])

    print("\n=== Answer ===")
    print(result["answer"])