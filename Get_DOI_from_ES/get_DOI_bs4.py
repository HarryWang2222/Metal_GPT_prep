from bs4 import BeautifulSoup
import lxml
import requests

total_page = 1
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'}


for page in range(0,total_page):
    offset = page * 100
    url = 'https://www.sciencedirect.com/search?pub=Materials%20Science%20and%20Engineering%3A%20A&show=100&offset='+str(offset)
    resp = requests.get(url, headers=header)
    html = resp.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    f = open('html.txt', 'w', encoding='utf-8')
    print(soup.prettify(), file = f)
    f.close()
    DOI_list = soup.find_all(class_ = 'ResultItem col-xs-24 push-m')
    print(DOI_list)


