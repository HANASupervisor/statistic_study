import numpy as np
import chromadb
from sentence_transformers import SentenceTransformer


# ============================================
# 1. ChromaDB 클라이언트 및 Collection 생성
# ============================================
def create_collection(
    db_path: str,
    collection_name: str
):
    # 1. ChromaDB 클라이언트 생성
    client = chromadb.PersistentClient(
        path=db_path
    )

    # 2. Collection 생성 또는 불러오기
    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "l2"}
    )

    return collection


# ============================================
# 2. 데이터 저장
# ============================================
def save_documents(
    collection, # ChromaDB Collection 객체
    model: SentenceTransformer, # 문장을 벡터로 변환하는 임베딩 모델
    chunks: list[str], # 분할된 문서들의 리스트
    metadata: list[dict] # 각 Chunk에 대응하는 메타데이터 리스트
):
    # Step 1. 각 Chunk의 고유 ID 생성
    ids = [
        f"travel_policy_article_{i + 1}"
        for i in range(len(chunks))
    ]
    # Step 2. 문서 임베딩
    embeddings = model.encode(chunks)
    # Step 3. 임베딩 자료구조 변환
    embeddings = np.asarray(
        embeddings,
        dtype=np.float32
    )
    # Step 4. ChromaDB에 데이터 저장
    collection.upsert(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=chunks,
        metadatas=metadata
    )

    return ids


# ============================================
# 3. 검색
# ============================================
def search_chroma(
    collection, # 검색할 ChromaDB Collection 객체
    model: SentenceTransformer, # 질문을 벡터로 변환할 임베딩 모델
    query: str, # 사용자가 입력한 질문 문자열
    k: int = 3 # 검색할 문서 개수(기본값 3)
):
    # STEP 1. 사용자 질문을 임베딩 벡터로 변환
    query_embedding = model.encode([query])

    # STEP 2. 임베딩 결과를 float32 NumPy 배열로 변환
    query_embedding = np.asarray(
        query_embedding,
        dtype=np.float32
    )

    # STEP 3. ChromaDB에서 유사한 문서 검색
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=min(k, collection.count()),
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    # STEP 4. 검색 결과 반환
    return results


# ============================================
# 4. 실행
# ============================================
if __name__ == "__main__":

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    chunks = [
        "출장을 진행하기 전에 부서장의 승인을 받아야 한다.",
        "교통비와 식비는 회사 규정에 따라 실비 정산한다.",
        "숙박비는 1박당 최대 10만 원까지 지원한다.",
        "출장 후 7일 이내에 영수증을 제출해야 한다."
    ]

    metadata = [
        {"source": "travel_policy.txt", "article": i + 1}
        for i in range(len(chunks))
    ]

    collection = create_collection(
        db_path="./chroma_exam_db",
        collection_name="travel_policy"
    )

    ids = save_documents(
        collection,
        model,
        chunks,
        metadata
    )

    print("저장 개수:", collection.count())

    query = "숙박비는 얼마까지 지원되나요?"

    results = search_chroma(
        collection,
        model,
        query,
        k=3
    )

    for rank, (doc_id, distance, doc, meta) in enumerate(
        zip(
            results["ids"][0],
            results["distances"][0],
            results["documents"][0],
            results["metadatas"][0]
        ),
        start=1
    ):
        print(f"\nRank {rank}")
        print("ID:", doc_id)
        print("Distance:", distance)
        print("Document:", doc)
        print("Metadata:", meta)