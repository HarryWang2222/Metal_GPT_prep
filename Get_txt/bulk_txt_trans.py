import os
import pdfplumber

folder_path = "H:/Metal GPT/literature/Acta Materialia"
year_start = 1997
year_end = 2020



for i in range(year_start, year_end):
    year = str(i)
    files_path = folder_path + '/' + year
    save_path = "H:/Metal GPT/text/Acta Materialia" + '/' + year + '/'

    files_list = []

    files = os.listdir(files_path)
    for file in files:
        file_path = files_path + '/' + str(file)
        files_list.append(file_path)

    print('Files_list obtained')

    counter = 0
    for single_file_path in files_list:
        with pdfplumber.open(single_file_path) as pdf:
            pdf_name = str(counter)
            counter = counter + 1
            save_name = "./output/Acta/" + year +"/" + pdf_name +'.txt'
            with open(save_name, "w", encoding='utf-8') as output:
                for page_num in range(0, len(pdf.pages)):
                    page = pdf.pages[page_num]
                    txt = page.extract_text_simple(x_tolerance=3, y_tolerance=3)
                    print(txt, file=output)
    print(year + 'done')
