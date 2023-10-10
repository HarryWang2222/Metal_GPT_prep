import os
from pypdf import PdfReader
from tqdm import tqdm



folder_path = "H:\\Metal GPT\\books\\"

files_path = folder_path
save_path = "H:\\Metal GPT\\text\\books\\"

files_list = [[],[]]

files = os.listdir(files_path)
for file in files:
    file_path = files_path + '\\' + str(file)
    files_list[0].append(str(file))
    files_list[1].append(file_path)

print('Files_list obtained')
print('txt conversion start')


for single_file_path in tqdm(files_list[1], leave=True):
    file_num = files_list[1].index(single_file_path)
    pdf_name = files_list[0][file_num]
    try:
        pdf = PdfReader(single_file_path)
        save_name = save_path + pdf_name + '.txt'
        with open(save_name, "w+", encoding='utf-8') as output:
            for page_num in range(0, len(pdf.pages)):
                page = pdf.pages[page_num]
                txt = page.extract_text()
                print(txt, file=output)
    except Exception as e:
        pass
    continue

print('books conversion done!')
