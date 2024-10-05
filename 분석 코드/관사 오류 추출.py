import spacy
from collections import Counter

# spaCy의 영어 모델 불러오기
nlp = spacy.load("en_core_web_sm")

# spaCy의 최대 입력 길이 설정
nlp.max_length = 15000000  # 필요한 길이로 설정

# 파일 읽기
with open('가천대 코퍼스.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 텍스트를 청크로 나누는 함수
def chunk_text(text, size):
    for i in range(0, len(text), size):
        yield text[i:i + size]

chunk_size = 10000  # 각 청크의 크기 설정
token_counts = Counter()

# 텍스트를 청크로 나누어 처리
for chunk in chunk_text(text, chunk_size):
    doc = nlp(chunk)
    tokens = [token.text for token in doc]
    token_counts.update(tokens)

# 결과를 텍스트 파일에 저장
with open('token_counts.txt', 'w', encoding='utf-8') as output_file:
    for token, count in token_counts.items():
        output_file.write(f"{token}: {count}\n")

print("토큰 빈도 결과가 token_counts.txt 파일에 저장되었습니다.")
