#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @created by CYang on 17:55 2023/5/18 0018
# @File: parse_pdf.py


import pdfplumber


def parse_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        # 获取第一页
        first_page = pdf.pages[0]

        # 提取文本内容
        text = first_page.extract_text()
        print(text)
        # 在文本中查找特定内容
        if "特定内容" in text:
            # 执行你想要的操作
            print("找到了特定内容！")
        else:
            print("未找到特定内容！")

# 指定PDF文件路径
pdf_file = "D:\\pythoncode\\crawler\\Cookie-analysis\\cookiebot扫描结果\\2-wwwalibabacom-16153457.pdf"

# 调用解析函数
parse_pdf(pdf_file)
