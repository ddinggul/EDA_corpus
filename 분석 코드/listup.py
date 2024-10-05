import nltk
from collections import Counter
import os


# NLTK 패키지를 처음 사용하는 경우, 아래 주석을 해제하여 필요한 데이터를 다운로드합니다.
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def extract_common_verbs_adjectives(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 텍스트를 토큰화합니다.
    tokens = nltk.word_tokenize(text.lower())

    # 각 토큰에 품사 태깅을 수행합니다.
    tagged_tokens = nltk.pos_tag(tokens)

    # 동사(VB로 시작하는 태그)와 형용사(JJ로 시작하는 태그)를 추출합니다.
    verbs = [word for word, pos in tagged_tokens if pos.startswith('VB')]
    adjectives = [word for word, pos in tagged_tokens if pos.startswith('JJ')]

    # 가장 빈번한 동사와 형용사 50개씩 추출합니다.
    common_verbs = Counter(verbs).most_common(50)
    common_adjectives = Counter(adjectives).most_common(50)

    return common_verbs, common_adjectives


def save_to_file(file_path, common_verbs, common_adjectives):
    base_name = os.path.basename(file_path)
    output_file_path = f"추출_{base_name}"

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write("Most Common Verbs:\n")
        for verb, freq in common_verbs:
            file.write(f"{verb}: {freq}\n")

        file.write("\nMost Common Adjectives:\n")
        for adjective, freq in common_adjectives:
            file.write(f"{adjective}: {freq}\n")


# 파일 경로를 여기에 입력하세요.
file_path = '/Users/junseo/PycharmProjects/Corpus_Analysis/가천대 코퍼스.txt'

common_verbs, common_adjectives = extract_common_verbs_adjectives(file_path)
save_to_file(file_path, common_verbs, common_adjectives)

print(f"Results saved to 추출_{os.path.basename(file_path)}")
