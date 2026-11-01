import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from pprint import pprint

'''
문서 저장 단계
1. document - 원본 문서
2. chunking - 문서를 작은 단위로 분할
3. Embedding - 문장을 숫자 벡터로 변환
4. FAISS Index / ChromaDB Collection - 저장

질문 검색 단계
1. Query - 사용자 질문
2. Query Embedding - 같은 모델로 벡터 변환
3. Similarity Search - 가까운 벡터 Top-K 검색
4. Retrieval Result - 원문 및 메타데이터 반환
'''

# 1. 임베딩 모델 생성
def load_model(model_name: str) -> SentenceTransformer:
    model = SentenceTransformer(model_name)
    return model

# [INPUT 예시]
model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# [함수 실행]
model = load_model(model_name)

# [OUTPUT 확인]
print("\n===== 1. load_model() =====")
print("INPUT:", model_name)
print("OUTPUT:", model)
print("OUTPUT TYPE:", type(model))
print("임베딩 차원:", model.get_sentence_embedding_dimension())

# OUTPUT:
# SentenceTransformer 객체
# 임베딩 차원: 384


# 2. 문서 chunking
def create_chunks(document: str) -> list[str]:
    """
    Args:
        document (str): 원본 문서

    Returns:
        list[str]: 분할된 문서 리스트
    """
    chunks =[
        chunk.strip()
        for chunk in document.strip().split("\n\n")
        if chunk.strip()
    ]
    return chunks

# [INPUT 예시]
document = """
제1조 출장 신청
직원은 출장 전에 승인을 받아야 한다.

제2조 출장비
교통비와 식비는 실비로 정산한다.

제3조 숙박비
숙박비는 최대 10만 원까지 지원한다.
"""

# [함수 실행]
chunks = create_chunks(document)

# [OUTPUT 확인]
print("\n===== 2. create_chunks() =====")
print("INPUT:", repr(document))
print("OUTPUT:")
pprint(chunks)
print("OUTPUT TYPE:", type(chunks))
print("청크 개수:", len(chunks))

# OUTPUT:
# [
#   '제1조 출장 신청\n직원은 출장 전에 승인을 받아야 한다.',
#   '제2조 출장비\n교통비와 식비는 실비로 정산한다.',
#   '제3조 숙박비\n숙박비는 최대 10만 원까지 지원한다.'
# ]




# 3. Metadata 생성
def create_metadata(chunks: list[str]) -> list[dict]:
    metadata = [
        {
            'source': 'travel_policy.txt',
            'article': i + 1
        }
        for i in range(len(chunks))
    ]
    return metadata

# [INPUT 예시]
# chunks = [
#     '제1조 출장 신청\n직원은 출장 전에 승인을 받아야 한다.',
#     '제2조 출장비\n교통비와 식비는 실비로 정산한다.',
#     '제3조 숙박비\n숙박비는 최대 10만 원까지 지원한다.'
# ]

# [함수 실행]
metadata = create_metadata(chunks)

# [OUTPUT 확인]
print("\n===== 3. create_metadata() =====")
print("INPUT:")
pprint(chunks)
print("OUTPUT:")
pprint(metadata)
print("OUTPUT TYPE:", type(metadata))

# OUTPUT:
# [{'article': 1, 'source': 'travel_policy.txt'},
#  {'article': 2, 'source': 'travel_policy.txt'},
#  {'article': 3, 'source': 'travel_policy.txt'}
# ]


# 4. 문서 임베딩
def embed_documents(model: SentenceTransformer, chunks: list[str], normalize: bool = False) -> np.ndarray:
    embeddings = model.encode(chunks, convert_to_numpy=True).astype('float32')

    if normalize:
        faiss.normalize_L2(embeddings)

    return embeddings


# [INPUT 예시]
# model = SentenceTransformer 객체
# chunks = 문서 3개가 들어 있는 list[str]
normalize = True

# [함수 실행]
embeddings = embed_documents(
    model=model,
    chunks=chunks,
    normalize=normalize
)

# [OUTPUT 확인]
print("\n===== 4. embed_documents() =====")
print("INPUT chunks:")
pprint(chunks)
print("INPUT normalize:", normalize)

print("OUTPUT SHAPE:", embeddings.shape)
print("OUTPUT TYPE:", type(embeddings))
print("OUTPUT DTYPE:", embeddings.dtype)
print("첫 번째 문서 임베딩 앞 10개:", embeddings[0][:10])
print("전체 벡터 길이:", np.linalg.norm(embeddings, axis=1))

# OUTPUT:
# SHAPE: (3, 384)
# TYPE: numpy.ndarray
# DTYPE: float32
# 첫 번째 문서 임베딩: [실수, 실수, 실수, ...]
# 정규화한 벡터의 L2 길이: 약 1.0


# 5. FAISS Index 생성 및 저장
def build_faiss_index(embeddings: np.ndarray, metric: str = 'l2') -> faiss.Index:
    # 벡터의 차원
    dimension = embeddings.shape[1]

    if metric == 'l2':
        index = faiss.IndexFlatL2(dimension)

    elif metric == 'ip':
        index = faiss.IndexFlatIP(dimension)

    else:
        raise ValueError('metric은 l2 또는 ip여야 합니다.')

    # 벡터 추가
    index.add(embeddings)
    return index


# [INPUT 예시]
# embeddings.shape = (3, 384)
metric = "ip"

# [함수 실행]
index = build_faiss_index(
    embeddings=embeddings,
    metric=metric
)

# [OUTPUT 확인]
print("\n===== 5. build_faiss_index() =====")
print("INPUT embeddings.shape:", embeddings.shape)
print("INPUT metric:", metric)

print("OUTPUT:", index)
print("OUTPUT TYPE:", type(index))
print("저장된 벡터 개수:", index.ntotal)
print("벡터 차원:", index.d)
print("첫 번째 저장 벡터 앞 10개:", index.reconstruct(0)[:10])

# OUTPUT:
# FAISS IndexFlatIP 객체
# index.ntotal = 3
# index.d = 384



# 6. Query 임베딩
def embed_query(model: SentenceTransformer, query: str, normalize: bool = False) -> np.ndarray:
    query_vector = model.encode([query], convert_to_numpy=True).astype('float32')

    if normalize:
        faiss.normalize_L2(query_vector)

    return query_vector


# [INPUT 예시]
query = "출장 숙박비는 얼마까지 지원되나요?"

# [함수 실행]
query_vector = embed_query(
    model=model,
    query=query,
    normalize=True
)

# [OUTPUT 확인]
print("\n===== 6. embed_query() =====")
print("INPUT:", query)
print("OUTPUT SHAPE:", query_vector.shape)
print("OUTPUT TYPE:", type(query_vector))
print("OUTPUT DTYPE:", query_vector.dtype)
print("OUTPUT 앞 10개:", query_vector[0][:10])

# OUTPUT:
# SHAPE: (1, 384)
# TYPE: numpy.ndarray
#
# 문서는 3개 -> (3, 384)
# 질문은 1개 -> (1, 384)


# 7. FAISS 검색
def search_faiss(index: faiss.Index, query_vector: np.ndarray, k: int = 3) -> tuple[np.ndarray, np.ndarray]:
    k = min(k, index.ntotal)

    distances, indices = index.search(query_vector, k)

    return distances, indices


# [INPUT 예시]
# index = 문서 3개가 저장된 FAISS 인덱스
# query_vector.shape = (1, 384)
k = 3

# [함수 실행]
distances, indices = search_faiss(
    index=index,
    query_vector=query_vector,
    k=k
)

# [OUTPUT 확인]
print("\n===== 7. search_faiss() =====")
print("INPUT index.ntotal:", index.ntotal)
print("INPUT query_vector.shape:", query_vector.shape)
print("INPUT k:", k)

print("OUTPUT distances:", distances)
print("OUTPUT indices:", indices)

print("distances.shape:", distances.shape)
print("indices.shape:", indices.shape)

# OUTPUT 예시 (실제 숫자는 실행 결과에 따라 다름):
#
# distances = [[0.85, 0.54, 0.32]]
# indices   = [[2, 1, 0]]
#
# distances: 유사도 점수
# indices: FAISS에 저장된 문서 위치
#
# IP + 정규화: 점수가 높을수록 유사함
# L2: 거리가 작을수록 유사함



# 8. 검색 결과와 원본 문서 매핑
def format_results(
    distances: np.ndarray,
    indices: np.ndarray,
    chunks: list[str],
    metadata: list[dict]
) -> list[dict]:

    results = []

    for rank, (idx, score) in enumerate(zip(indices[0], distances[0]), start=1):
        idx = int(idx)

        if idx < 0:
            continue

        results.append({
            "rank": rank,
            "document_id": idx,
            "score": float(score),
            "text": chunks[idx],
            "metadata": metadata[idx]
        })
    return results


# [INPUT 예시]
# distances = [[0.85, 0.54, 0.32]]  <- 실제 검색 점수 사용
# indices   = [[2, 1, 0]]           <- 실제 검색 인덱스 사용
# chunks    = 문서 원본 리스트
# metadata  = 문서 메타데이터 리스트

# [함수 실행]
results = format_results(
    distances=distances,
    indices=indices,
    chunks=chunks,
    metadata=metadata
)

# [OUTPUT 확인]
print("\n===== 8. format_results() =====")
print("INPUT distances:", distances)
print("INPUT indices:", indices)
print("OUTPUT:")
pprint(results, sort_dicts=False)
print("OUTPUT TYPE:", type(results))

# OUTPUT 구조 예시:
#
# [
#   {
#       'rank': 1,
#       'document_id': 2,
#       'score': 0.85,
#       'text': '제3조 숙박비\n숙박비는 최대 10만 원까지 지원한다.',
#       'metadata': {
#           'source': 'travel_policy.txt',
#           'article': 3
#       }
#   },
#   ...
# ]


# ============================================
# 9. 전체 실행
# ============================================
if __name__ == "__main__":

    document = """
    제1조 출장 신청
    직원은 출장을 진행하기 전에 부서장의 사전 승인을 받아야 한다.

    제2조 출장비
    출장 중 발생한 교통비와 식비는 회사 규정에 따라 실비로 정산한다.

    제3조 숙박비
    출장 시 숙박비는 1박당 최대 10만 원까지 지원한다.

    제4조 정산 절차
    출장을 마친 직원은 7일 이내에 영수증과 출장 보고서를 제출해야 한다.

    제5조 해외 출장
    해외 출장 시 항공권과 숙박비는 별도의 해외 출장 규정에 따른다.
    """

    model = load_model(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    chunks = create_chunks(document)
    metadata = create_metadata(chunks)

    # IP + 정규화를 사용하면 코사인 유사도로 검색
    embeddings = embed_documents(
        model,
        chunks,
        normalize=True
    )

    index = build_faiss_index(
        embeddings,
        metric="ip"
    )

    query = "출장 숙박비는 얼마까지 지원되나요?"

    query_vector = embed_query(
        model,
        query,
        normalize=True
    )

    distances, indices = search_faiss(
        index,
        query_vector,
        k=3
    )

    results = format_results(
        distances,
        indices,
        chunks,
        metadata
    )

    print("Chunk 개수:", len(chunks))
    print("Embedding Shape:", embeddings.shape)
    print("Query Shape:", query_vector.shape)
    print("저장된 벡터:", index.ntotal)

    for result in results:
        print("\n", result)