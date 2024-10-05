import os


# 인코딩 변경 함수
def convert_encoding_to_utf8(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='ISO-8859-1') as file:
        text = file.read()

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# 디렉터리 내 모든 파일의 인코딩을 변경하는 함수
def convert_all_files_in_directory(input_directory, output_directory):
    # 출력 디렉터리가 없으면 생성합니다.
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename)

        # 파일 인코딩을 변경합니다.
        convert_encoding_to_utf8(input_file_path, output_file_path)
        print(f"File {filename} encoding converted and saved to {output_file_path}")


# 입력 디렉터리와 출력 디렉터리를 지정합니다.
input_directory = '/Users/junseo/PycharmProjects/Corpus_Analysis/LOCNESS-corpus-files 복사본'
output_directory = '/Users/junseo/PycharmProjects/Corpus_Analysis/raw_data'

# 모든 파일의 인코딩을 변경합니다.
convert_all_files_in_directory(input_directory, output_directory)
