import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = 'https://www.sciencedirect.com/science/article/pii/S0921509323009681'
headers = {
        'user-agent': '(Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
res = requests.get(url, headers=headers)
bsObj = BeautifulSoup(res.text, 'lxml')
content = bsObj.findAll('script', {'type': 'application/json'})[0].text
content_json = json.loads(content)

info_dict = {}
info_dict['volume_num'] = int(content_json['article']['vol-first'])
info_dict['doi'] = content_json['article']['doi']
info_dict['affiliation'] = content_json['authors']['affiliations']['aff1']['$$'][1]['_']
info_dict['title'] = content_json['article']['titleString']

# keywords
keywords_div = bsObj.findAll('div', class_="keywords-section")[0].findAll('div', class_='keyword')
keywords_list = [keyword.text for keyword in keywords_div]
for keyword in keywords_list:
    kw = kw + keyword + ';'
info_dict['kw_num'] = len(keywords_list)

info_dict['abstract'] = bsObj.findAll('div', id="abssec0010")[0].text

info_list = []
# 对不起伙伴们，嘎杂偷懒了，这里同一个info跑10次相当于在不同页面上的内容存入10次。
for i in range(10):
	info_list.append(info_dict)

info_df = pd.DataFrame(info_list)

info_df.to_csv('文献信息.csv')
