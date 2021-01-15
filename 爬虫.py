#作者:邢洪盛 本人是一个python小白代码严禁用于非法用途后果自负
''''请求网页'''
import os

import requests
import re\
   #导入re请求库
#导入一个请求库（请注意quests库需要在cmd命令提示符上使用：“pip install quests"命令来进行下载安装请求库
headers ={
    'User-Agent':'xxggusucgufhsjjdjd/xinfg/csmd/chrome1.21.24'
    #这里是使爬虫模拟正常浏览器的ua标志防止目标服务器反爬
}
response=requests.get('https://vmgirls.com/12985.html',headers=headers)
#这里是使用请求库进行得到一个目标网站的请求数据  后面加上”headers是为了找到目标网页的请求头也就是requests headers
print(response.text)
#这里打印一下请求库所概括的网页
print(response.request.headers)
#模拟正常浏览器

#解析网页
dir_name = re. findall('图片地址')[-1]
if not os.path.exists(dir_name):
    #这里的意思是检测是否存在os这个文件夹
    os.mkdir(dir_name)
    #这是创建一个dir_name的这个文件夹
urls = re.findell('输入图片的')
#方便一会在下面打印urls
print (urls)


#保存图片↓
for url in urls:
    #图片名字
    file_name = url.split('/')[-1]
    response = requests.get(url,header=headers)
    with open(dir_name+'/'+file_name,'wb') as f:
        #这里是将所爬下的内容下载到所创建的dir_name文件夹，中间的'/’是替换的文件的意思
        f.write(response.content)




