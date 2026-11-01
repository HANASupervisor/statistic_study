
from pathlib import Path
from pypdf import PdfReader
import re
import json


# ============================================
# 1. PDF 파일 경로 확인
# ============================================
def check_pdf_path(pdf_path: str) -> Path:
    """
    Input:
        pdf_path: str (PDF 파일 경로)

    Output:
        Path (검증된 파일 경로)
    """

    # STEP 1. 문자열 경로를 Path 객체로 변환
    path = Path(pdf_path)

    # STEP 2. 실제 파일이 존재하는지 확인
    if not path.is_file():
        raise FileNotFoundError(f"PDF 파일 없음: {path}")

    # STEP 3. 검증된 경로 반환
    return path


# ============================================
# 2. PDF 전체 페이지 텍스트 추출
# ============================================
def extract_pdf_text(pdf_path: str) -> list[str]:
    """
    Input:
        pdf_path: str

    Output:
        list[str]: 페이지별 텍스트
    """

    # STEP 1. PDF 파일 존재 확인
    path = check_pdf_path(pdf_path)

    # STEP 2. PDF 파일 열기
    reader = PdfReader(str(path))

    # STEP 3. 페이지별 텍스트 저장 리스트 생성
    all_text = []

    # STEP 4. PDF의 모든 페이지 순회
    for page in reader.pages:

        # STEP 5. 현재 페이지에서 텍스트 추출
        # 추출 결과가 None이면 빈 문자열로 대체
        text = page.extract_text() or ""

        # STEP 6. 추출한 텍스트를 리스트에 저장
        all_text.append(text)

    return all_text


# ============================================
# 3. Text Cleaning
# ============================================
def clean_text(text: str) -> str:
    """
    Input:
        text: str (Raw Text)

    Output:
        str (정리된 텍스트)
    """

    # STEP 1. 연속된 공백과 탭을 공백 하나로 변경
    text = re.sub(r"[ \t]+", " ", text)

    # STEP 2. 3개 이상 연속된 줄바꿈을 2개로 변경
    text = re.sub(r"\n{3,}", "\n\n", text)

    # STEP 3. 문자열 양쪽 공백 및 줄바꿈 제거
    text = text.strip()

    return text


# ============================================
# 4. 페이지별 Metadata 생성
# ============================================
def create_documents(
    texts: list[str],
    pdf_path: str
) -> list[dict]:
    """
    Input:
        texts: list[str]
        pdf_path: str

    Output:
        list[dict]: 페이지별 Document와 Metadata
    """

    # STEP 1. PDF 파일명과 제목 추출
    path = Path(pdf_path)
    file_name = path.name
    title = path.stem

    # STEP 2. 전체 페이지 수 계산
    total_pages = len(texts)

    # STEP 3. Document를 저장할 리스트 생성
    documents = []

    # STEP 4. 각 페이지의 텍스트를 순회
    for page_index, text in enumerate(texts):

        # STEP 5. 현재 페이지의 Metadata 생성
        metadata = {
            "source": file_name,
            "page": page_index,
            "total_pages": total_pages,
            "title": title
        }

        # STEP 6. 텍스트와 Metadata를 하나로 묶기
        document = {
            "page_content": text,
            "metadata": metadata
        }

        # STEP 7. 전체 Document 리스트에 추가
        documents.append(document)

    return documents


# ============================================
# 5. JSON 파일 저장
# ============================================
def save_json(
    documents: list[dict],
    output_path: str
) -> None:

    # STEP 1. UTF-8 인코딩으로 파일 열기
    with open(output_path, "w", encoding="utf-8") as f:

        # STEP 2. Python 객체를 JSON 형식으로 저장
        json.dump(
            documents,
            f,
            ensure_ascii=False,
            indent=2
        )


# ============================================
# 6. TXT 파일 저장
# ============================================
def save_txt(
    documents: list[dict],
    output_path: str
) -> None:

    # STEP 1. 텍스트 파일 열기
    with open(output_path, "w", encoding="utf-8") as f:

        # STEP 2. 각 페이지의 Document 순회
        for doc in documents:

            # STEP 3. 페이지 번호와 원본 텍스트 추출
            page_number = doc["metadata"]["page"] + 1
            text = doc["page_content"]

            # STEP 4. 페이지 구분자와 본문 저장
            f.write(f"===== Page {page_number} =====\n")
            f.write(text)
            f.write("\n\n")


# ============================================
# 7. JSON 파일 다시 불러오기
# ============================================
def load_json(json_path: str) -> list[dict]:

    # STEP 1. JSON 파일 열기
    with open(json_path, "r", encoding="utf-8") as f:

        # STEP 2. JSON을 Python 객체로 변환
        documents = json.load(f)

    return documents


# ============================================
# 8. 전체 PDF 전처리 파이프라인
# ============================================
def preprocess_pdf(pdf_path: str) -> list[dict]:

    # STEP 1. PDF 페이지별 Raw Text 추출
    all_text = extract_pdf_text(pdf_path)

    # STEP 2. 추출한 모든 텍스트 Cleaning
    cleaned_texts = [
        clean_text(text)
        for text in all_text
    ]

    # STEP 3. Metadata를 포함한 Document 생성
    documents = create_documents(
        cleaned_texts,
        pdf_path
    )

    return documents


# ============================================
# 9. 메인 프로그램 실행
# ============================================
if __name__ == "__main__":

    # STEP 1. 현재 Python 파일이 있는 폴더 기준 경로
    base_dir = Path(__file__).resolve().parent

    pdf_path = base_dir / "company_policy.pdf"
    json_path = base_dir / "pdf_result.json"
    txt_path = base_dir / "pdf_result.txt"

    # STEP 2. PDF 추출 + Cleaning + Metadata 생성
    documents = preprocess_pdf(str(pdf_path))

    # STEP 3. JSON 및 TXT 저장
    save_json(documents, str(json_path))
    save_txt(documents, str(txt_path))

    # STEP 4. JSON 다시 읽기
    loaded_documents = load_json(str(json_path))

    # STEP 5. 결과 검증
    assert len(documents) == len(loaded_documents)
    assert documents == loaded_documents

    print("Document 개수:", len(documents))

    for doc in documents:
        print("\nMetadata:", doc["metadata"])
        print("본문:", doc["page_content"][:100])

    print("\nPDF 전처리 완료!")
