import requests
import sys

# 'https://api.jisuapi.com/xiaohua/text'

url = 'https://api.jisuapi.com/xiaohua/text'
headers = {'User-Agent':'Mozilla/5.0'}
params = {
    # 'key':'36de5db81215'
    'pagenum':'1',
    'pagesize':'1',
    'sort':'addtime',
    'key':'c812e10685414c68'
}

try:
    res = requests.get(url,params=params,headers=headers,timeout=10)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'请求异常: {e}')
    sys.exit()
else:
    json = res.json()
    print(json)
    # print(json['result']['list'][0]['content'])