# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:19:21 2021

@author: xyyx
"""
#############################################
#   PyPDF2太过粗糙，无法获取全部pdf全文内容
#############################################
# (1) a function to locate the string
# pip install PyPDF2
def fnPDF_FindText(xFile, xString):
    # xfile : the PDF file in which to look
    # xString : the string to look for
    from PyPDF2 import PdfFileReader, PdfFileWriter
    import re
    
    pdfDoc = PdfFileReader(open(xFile,'rb'))  # 打开pdf对象
    pdfPages = pdfDoc.getNumPages()  # 获取pdf总页数
    print("该文件共%s页" %pdfPages)
    documentInfo = PdfFileReader.getDocumentInfo(pdfDoc) # 获取 PDF 文件的文档信息
    print('documentInfo = %s' % documentInfo)
    PageFound = -1
    for i in range(0, pdfPages):
        '''循环每一页'''
        content = ""
        content += pdfDoc.getPage(i).extractText() + "\n"   # 把pdf第i页的文本全部拼接为一个字符串content
        # print(content)
        content1 = content.encode('ascii', 'ignore').decode().lower() # 替换为小写
        # content1 = content.lower()
        print(content1)
        ResSearch = re.search(xString, content1)  # 从content中搜索指定字符串
        
        if ResSearch is not None:
            '''如果搜索成功，则返回指定字符串第一次出现的页码。'''
            PageFound = i+1
            print(xString,"在第%页" % PageFound)
            break
        else:
            page = i + 1
            print("第%s页未找到" %page,xString)
    return PageFound

import os
path = r"D:\tempro\TeacherXu"
os.chdir(r"D:\tempro\TeacherXu")
# xFile = "./Tradable-performance-standards-in-the-transportation-sec_2021_Energy-Economi.pdf"
xFile = "./q.pdf"
xString = "instrument variables"
PageFound = fnPDF_FindText(xFile, xString)
##########################################
# PDF-->HTML
##########################################

import os
import winerror
from win32com.client.dynamic import Dispatch, ERRORS_BAD_CONTEXT

ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)
ori_path = r"D:\tempro\TeacherXu"
os.chdir(r"D:\tempro\TeacherXu")
my_dir = ori_path #你放参考文献pdf的路径

pdf_list = [pdf for pdf in os.listdir(my_dir) if pdf[-3:] == "pdf"] #列出文件夹下所有的目录与文件
for i in range(0,len(pdf_list)):
        AvDoc = Dispatch("AcroExch.AVDoc")
        path = os.path.join(my_dir,pdf_list[i])
        # print(os.path.join("D:\\download\\综述参考文献html", list[i][0:-3]+"html"))
        if os.path.isfile(path):
            # os.chdir(r"D:\\download\\综述参考文献")
            src = os.path.abspath(pdf_list[i])
            try:
                if AvDoc.Open(src, ""):
                    pdDoc = AvDoc.GetPDDoc()
                    jsObject = pdDoc.GetJSObject()
                    jsObject.SaveAs(os.path.join(ori_path, pdf_list[i][0:-3]+"html"), "com.adobe.acrobat.html")#你放html的路径
            except Exception as e:
                print(str(e))
                AvDoc.Close(True)
            finally:
                jsObject = None
                pdDoc = None
                AvDoc = None
print("--------------------结束啦---------------------")
AvDoc.Close(True)




