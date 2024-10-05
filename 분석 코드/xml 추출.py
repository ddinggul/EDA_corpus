import os
import xml.etree.ElementTree as ET


def extract_body_texts_from_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        body_elements = root.findall('.//body')

        body_texts = []
        for body in body_elements:
            body_text = ''.join(body.itertext()).strip()

            if len(body_text) >= 10 and 'head:' not in body_text.lower():
                body_texts.append(body_text)

        return body_texts
    except ET.ParseError as e:
        print(f"Error parsing {file_path}: {e}")
        return []


def extract_and_save_all_bodies(directory_path, output_file):
    all_body_texts = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory_path, filename)
            body_texts = extract_body_texts_from_xml(file_path)
            all_body_texts.extend(body_texts)

    with open(output_file, 'w', encoding='utf-8') as f:
        for idx, body in enumerate(all_body_texts):
            f.write(f"Body {idx + 1}:\n")
            f.write(body + "\n\n")


directory_path = '/Users/junseo/PycharmProjects/Corpus_Analysis/xml'
output_file = 'BT_all_bodies.txt'

extract_and_save_all_bodies(directory_path, output_file)

print(f"All body texts have been extracted and saved to {output_file}")
