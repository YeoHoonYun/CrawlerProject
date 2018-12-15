# -*- coding: utf-8 -*-
from db_connect import mysql_test
from data_cralwer import crawler
from datetime import datetime
import socket, xlsxwriter, time

def creat_xlsx(gisa_list):
    workbook = xlsxwriter.Workbook(r'./text.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    first = ['keyword', 'title', 'writer', 'contnet', 'url', 'cal']
    for text in first:
        worksheet.write(row, col, text)
        col += 1
    row += 1
    col = 0
    for gisa in gisa_list:
        for value in gisa.values():
            try:
                worksheet.write(row, col, value)
            except:
                value = ",".join(value)
                worksheet.write(row, col, value)
            col += 1
        row += 1
        col = 0
    workbook.close()

if __name__ == '__main__':
    gisa_list = []
    print (socket.gethostbyname(socket.gethostname()))
    my_ip = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("""127.""")][:1][0]

    while True:
        db = mysql_test(host = "210.92.91.236", user = "root",password= "hadoop", db = "yun")
        keywords = db.keyword_get(type = "SELECT", query="SELECT user, pw, keyword, start_cal, stop_cal FROM main_db WHERE crawler_ip = %s AND flag=0", val = ('192.168.4.81'))
        page = "250"
        print(keywords)
        for i in keywords:
            crawler = crawler(page, db)
            gisa_list = crawler.daum(i[0], i[2], str(i[3]).replace('-',''), str(i[4]).replace('-',''))
            db.keyword_get(type="UPDATE", query="UPDATE main_db SET flag=%s WHERE user=%s AND keyword=%s;", val=(1, i[0], i[2]))

            for j in gisa_list:
                print(j['title'])

        creat_xlsx(gisa_list)
        time.sleep(300)