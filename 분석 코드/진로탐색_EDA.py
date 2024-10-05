import os
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd

# NLTK 데이터 다운로드 (최초 한 번만 실행)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# 텍스트 파일 불러오기 함수
def load_text_file(file_path, encoding='utf-8'):
    print(f"Loading file {file_path}...")
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    print(f"Loaded file {file_path}.")
    return text


# Word list 추출 함수
def extract_word_list(text):
    print("Extracting word list...")
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalpha()]
    print("Word list extracted.")
    return words


# 품사 태깅 함수
def pos_tagging(word_list):
    print("Tagging parts of speech...")
    tagged_words = nltk.pos_tag(word_list)
    print("Parts of speech tagged.")
    return tagged_words


# 'Adj + N' 형태의 collocation 추출 함수
def extract_adj_noun_collocations(tagged_words):
    print("Extracting Adj + N collocations...")
    collocations = []
    for i in range(len(tagged_words) - 1):
        if tagged_words[i][1] in ['JJ', 'JJR', 'JJS'] and tagged_words[i + 1][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
            collocations.append((tagged_words[i][0], tagged_words[i + 1][0]))
    print("Adj + N collocations extracted.")
    return collocations


# collocation 빈도수 계산 함수
def count_collocations(collocations):
    print("Counting collocation frequencies...")
    collocation_counter = Counter(collocations)
    print("Collocation frequencies counted.")
    return collocation_counter


# collocation을 엑셀 파일로 저장하는 함수
def save_collocations_to_excel(learners_collocation_counter, native_collocation_counter, output_file_path):
    print(f"Saving collocations to Excel file {output_file_path}...")

    learners_data = [{"Collocation": f"{coll[0]} {coll[1]}", "Frequency": freq} for coll, freq in
                     learners_collocation_counter.items()]
    native_data = [{"Collocation": f"{coll[0]} {coll[1]}", "Frequency": freq} for coll, freq in
                   native_collocation_counter.items()]

    learners_df = pd.DataFrame(learners_data).sort_values(by="Frequency", ascending=False)
    native_df = pd.DataFrame(native_data).sort_values(by="Frequency", ascending=False)

    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        learners_df.to_excel(writer, sheet_name='Learners', index=False)
        native_df.to_excel(writer, sheet_name='Native', index=False)

    print(f"Collocations saved to {output_file_path}")


# 입력 디렉터리를 지정합니다.
learners_directory = '/Users/junseo/PycharmProjects/Corpus_Analysis/raw_data/learners'
native_directory = '/Users/junseo/PycharmProjects/Corpus_Analysis/raw_data/native'
collocations_output_file = '/Users/junseo/PycharmProjects/Corpus_Analysis/collocations_output.xlsx'

# Learners 디렉터리의 모든 텍스트 파일을 불러와서 분석합니다.
learners_collocations = []
print("Processing learners files...")
for filename in os.listdir(learners_directory):
    file_path = os.path.join(learners_directory, filename)
    text = load_text_file(file_path, encoding='utf-8')

    # Word list 추출
    word_list = extract_word_list(text)

    # 품사 태깅
    tagged_words = pos_tagging(word_list)

    # 'Adj + N' 형태의 collocation 추출
    adj_noun_collocations = extract_adj_noun_collocations(tagged_words)
    learners_collocations.extend(adj_noun_collocations)

# Learners collocation의 빈도수를 계산합니다.
learners_collocation_counter = count_collocations(learners_collocations)

# Native 디렉터리의 모든 텍스트 파일을 불러와서 분석합니다.
native_collocations = []
print("Processing native files...")
for filename in os.listdir(native_directory):
    file_path = os.path.join(native_directory, filename)
    text = load_text_file(file_path, encoding='utf-8')

    # Word list 추출
    word_list = extract_word_list(text)

    # 품사 태깅
    tagged_words = pos_tagging(word_list)

    # 'Adj + N' 형태의 collocation 추출
    adj_noun_collocations = extract_adj_noun_collocations(tagged_words)
    native_collocations.extend(adj_noun_collocations)

# Native collocation의 빈도수를 계산합니다.
native_collocation_counter = count_collocations(native_collocations)

# collocation을 엑셀 파일로 저장합니다.
save_collocations_to_excel(learners_collocation_counter, native_collocation_counter, collocations_output_file)

print("Processing complete.")
