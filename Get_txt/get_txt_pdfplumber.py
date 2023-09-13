import pdfplumber

with pdfplumber.open("./data/test2.pdf") as pdf:
    with open('./output/out_plumber2.txt', 'w', encoding='utf-8') as output:
        for i in range(0,len(pdf.pages)):
            page = pdf.pages[i]
            print(page.find_tables(table_settings={}))
            # txt = page.extract_text_simple(x_tolerance=3, y_tolerance=3)
            # print(txt, file=output)
