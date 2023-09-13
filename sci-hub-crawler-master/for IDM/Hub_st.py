import requests
from bs4 import BeautifulSoup
import re

def download(doi, user_agent="wang", proxies=None, num_retries=2, start_url='sci-hub.ru'):
    headers = {'User-Agent': user_agent}
    url = 'https://{}/{}'.format(start_url, doi)
    print('Downloading: ', url)
    try:
        resp = requests.get(url, headers=headers, proxies=proxies, verify=False)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error: ', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                return download(url, user_agent, proxies, num_retries-1)
    except requests.exceptions.RequestException as e:
        print('Download error', e)
        return None
    return html


if __name__ == '__main__':
    doi = '10.1016/j.actamat.2020.10.014'
    print(download(doi))
