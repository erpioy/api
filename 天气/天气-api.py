import requests
import sys

url = 'https://whyta.cn/api/tianqi'
headers = {'User-Agent':'Mozilla/5.0'}
params = {
    'city':'苏州',
    'key':'36de5db81215'
    #'key':'c812e10685414c68'
}

try:
    res = requests.get(url,params=params,headers=headers,timeout=10)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'请求异常: {e}')
    sys.exit()
else:
    json = res.json()
    print(json['lives'])
    