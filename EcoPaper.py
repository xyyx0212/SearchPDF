# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:58:49 2021

@author: xyyx
"""
import os
import requests as req
import re
import time

path = r"D:\tempro\TeacherXu"
os.chdir(path)

SearchKey = "CSR"
url = "https://econpapers.repec.org/scripts/search.pf?ft={};pg=1".format(SearchKey)
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"
    }

url1 = "https://econpapers.repec.org/scripts/search.pf?ft=哈哈"
res = req.get(url,headers = headers,timeout = 5)
res.content.decode()
print(res.content)
def get_urls(SearchKey):
    # 判断搜索结果是否为空
    url = "https://econpapers.repec.org/scripts/search.pf?ft=CSR"
    headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"
    }
    LinkFlag = True
    while LinkFlag:
        try:
            res = req.get(url,headers = headers,timeout = 3)
            if res.status_code == 200:
                LinkFlag=False
        except:
            print("连接失败，重新连接。")
            time.sleep(10)
            
    if "No matching documents when searching for" in res.content.decode():
        print("搜索结果为空，请更换SearchKey。")
        # return 0
    else:
        str = res.content.decode()  #要decode()才能使用re
        pattern1 = re.compile(r'(?<=page\s1\sof\s)(\d*)')
        TotalPage = re.search(pattern1,str).group()   # 总页数无法使用xpath定位，使用正则
        url = "https://econpapers.repec.org/scripts/search.pf?ft={};pg=1".format(SearchKey)
        
        
            

    
