import requests

url = 'https://sci-hub.ru/10.1016/j.actamat.2020.10.014'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'}
re = requests.get(url, headers= headers, verify=False)
print(re.text)
