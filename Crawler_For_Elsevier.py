import requests
from bs4 import BeautifulSoup
import re


def download(doi, user_agent="sheng", proxies=None, num_retries=2, start_url='sci-hub.ren'):
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
                return download(url, user_agent, proxies, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error', e)
        return None
    return html

def get_link_using_bs4(html, parser='html5lib'):
    # parse the HTML
    try:
        soup = BeautifulSoup(html, parser)
    except:
        print('parser not available, now use the default parser "html.parser"...')
        parser = 'html.parser'
        soup = BeautifulSoup(html, parser)
    soup.prettify()
    div = soup.find('div', attrs={'id': 'buttons'})
    if div:
        a = div.find('a', attrs={'href': '#'})
        if a:
            a = a.attrs['onclick']
            return re.findall(r"location.href\s*=\s*'(.*?)'", a)[0]
    return None

def download_pdf(url, user_agent="sheng", proxies=None, num_retries=2):
    headers = {'User-Agent': user_agent}
    url = 'https:{}'.format(url)  # 改动1
    print('Downloading: ', url)
    try:
        resp = requests.get(url, headers=headers, proxies=proxies, verify=False)
        if resp.status_code >= 400:
            print('Download error: ', resp.status_code)
            if num_retries and 500 <= resp.status_code < 600:
                return download(url, user_agent, proxies, num_retries-1)
        #  ok, let's write it to file
        with open('file.pdf', 'wb') as fp:  # 改动2，注意 'wb' 而不是 'w'
            fp.write(resp.content)
    except requests.exceptions.RequestException as e:
        print('Download error', e)


if __name__ == '__main__':
    #from download import download
    dois = ['10.1016/j.apergo.2020.103286',  # VR
            '10.1016/j.jallcom.2020.156728',  # SOFC
            '10.3964/j.issn.1000-0593(2020)05-1356-06']  # 飞行器
    links = []
    for doi in dois:
        html = download(doi)
        #  print(html)
        link = get_link_using_bs4(html)
        if link:
            links.append(link)
    for link in links:
        print(link)
