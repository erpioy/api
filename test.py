import requests
from bs4 import BeautifulSoup
import sys
import re

content = ''
sort = 1

def get_film(url):
    global content,sort
    headers = {'User-Agent':'Mozilla/5.0'}
    try:
        res = requests.get(url,headers=headers,timeout=10)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'请求失败：{e}')
        sys.exit()
    else:
        html = res.text
        soup = BeautifulSoup(html,'html.parser')
        # lis = soup.find_all('li')
        # print(lis)
        #titles = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
        msgs = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p:nth-child(1)')
        
        #infos = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p.quote > span')
        
        
        # for title,msg,info in zip(titles,msgs,infos):
        #     director = re.findall(r'导演:\s*(.*?).*',msg.text)
        #     about = re.search(r'\d{4}.*',msg.text)
        #     content = content + '【' + str(sort) + '】' + '电影：' + title.text + ' 导演：' + director[0] + ' 年代及类型：' + about.group() + '\n'+ '引用：' + info.text + '\n'
        #     sort += 1

        # for title in titles:
        #     content += str(sort) + ': ' + title.text + '\n'
        #     sort += 1

        for msg in msgs:
            director = re.findall(r'导演:\s*(.*?)(?=\s*(主演:|[\d]{4}|$))',msg.text)
          
            content += str(sort) + ': ' + director[0][0] + '\n'
            sort += 1
for i in range(10):
    num = i * 25
    url = 'https://movie.douban.com/top250' + '?start=' + str(num)
    get_film(url)
print(content)


                            

                            
    

        