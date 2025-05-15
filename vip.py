import requests
from bs4 import BeautifulSoup
import sys
#获取html
url = 'https://www.baidu.com'
headers = {'User-Agent':'Mozilla/5.0'}


try:
    res = requests.get(url,headers=headers,timeout=10)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'请求异常: {e}')
    sys.exit()
else: 
    print(res.headers)




#解析html
#获取所需信息
#下载