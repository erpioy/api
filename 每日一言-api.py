import requests
import sys

# 'https://whyta.cn/api/yiyan'

url = 'https://whyta.cn/api/yiyan'
headers = {'User-Agent':'Mozilla/5.0'}
params = {
    'key':'36de5db81215'
}

try:
    res = requests.get(url,params=params,headers=headers,timeout=10)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'请求异常: {e}')
    sys.exit()
else:
    json = res.json()
    for key,value in json.items():
        print(f'{key}: {value}')
    