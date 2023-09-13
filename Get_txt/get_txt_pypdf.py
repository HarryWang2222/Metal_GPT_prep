from pypdf import PdfReader

reader = PdfReader("./data/test2.pdf")
number_of_pages = len(reader.pages)
with open('./output/out2.txt', 'w', encoding='utf-8')as output:
    for i in range(0,number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        print(text, file=output)
