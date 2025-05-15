import requests 
from lxml import html

url = input('输入歌曲列表链接：')

url = url.replace('/#','')
# 建立连接，获取该页面的html文档

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 
}
res = requests.get(url,headers=headers)


# 解析html
tree = html.fromstring(res.text)

# 获取所需信息
songs = tree.xpath('//a[contains(@href,"/song?id=")]')
for song in songs:
    song_href = song.xpath('./@href')[0]
    id = song_href.split('=')[1]
    title = song.xpath('./text()')[0]

    # 下载
    music_url = 'https://api.qijieya.cn/meting/?type=url&id=' + id
    music = requests.get(music_url,headers=headers)
    try:
        with open('./music/陈粒/%s.mp3' % title,'wb') as file:#创建一个空白的音乐文件
            file.write(music.content)
    #把从网页中获取的音乐数据写入到空白的音乐文件里
        print('《%s》下载成功'% title)
    except:
        print('22')
        break

