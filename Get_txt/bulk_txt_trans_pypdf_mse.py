import os
from pypdf import PdfReader
from tqdm import tqdm

# initial setup
journal_name = str('Materials Science and Engineering A')
year_start = 1999
year_end = 2020


folder_path = "H:\\Metal GPT\\literature\\"
folder_path = folder_path + journal_name


for i in range(year_start, year_end+1):
    year = str(i)
    files_path = folder_path + '\\' + year
    save_path = "H:\\Metal GPT\\text\\" + journal_name + '\\' + year + '\\'

    files_list = []

    files = os.listdir(files_path)
    for file in files:
        file_path = files_path + '\\' + str(file)
        files_list.append(file_path)

    print('Files_list obtained')
    print(year + 'start')

    counter = 0
    for single_file_path in tqdm(files_list, leave=True):
        pdf_name = str(counter)
        counter = counter + 1
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


    print(year + 'done')
