# import re
# import requests
#
# url ='https://api.bilibili.com/x/v1/dm/list.so?oid=31621681 '
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#           }
# req=requests.get(url,headers =header,verify=False).content.decode('utf-8')
#
#
#
# obj = re.findall(r'<d[\s\S]*?>([\s\S]*?)</d>',req,re.S)
#
# print(obj)
#

import requests
from lxml import etree

url='https://api.bilibili.com/x/v1/dm/list.so?oid=31621681'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
           }

req =requests.get(url=url,headers=headers,verify=False).content
tree = etree.HTML(req)
obj=tree.xpath('//d/text()')
with open('改革春风.txt','a',encoding='utf-8')as fp:
    for i in obj:
        fp.write(i+'\n')
