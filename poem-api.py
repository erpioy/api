import requests
import sys

# 国内使用 不需要参数
# 'https://v1.jinrishici.com/all.json'

url = 'https://v1.jinrishici.com/all.json'
headers = {'User-Agent':'Mozilla/5.0'}

try:
    res = requests.get(url,headers=headers,timeout=10)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'请求异常: {e}')
    sys.exit()
else:
    json = res.json()
    for key,value in json.items():
        print(f'{key}: {value}')
    