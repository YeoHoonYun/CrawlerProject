# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from konlpy_test import konlpy_test
import xlsxwriter
import requests, re, json, cal
# from kakfa_connect
# from db_connect import mysql
# import sqlite3, qpublic


class crawler:
    def __init__(self, page, db):
        self.type = 'daum_news'
        self.date_out = cal.date_out()
        self.kon = konlpy_test()
        self.page = page
        self.db = db

    def clean_text(self,text):
        text = re.sub(' ', '', text)
        text = re.sub('\t', '', text)
        text = re.sub('\n', '', text)
        text = text.split('|')
        return text

    def daum(self,user ,keyword, start_time, end_time):
        news_dict = {}
        gisa_list = []
        num = 1
        cur_cal = self.db.keyword_get(type = "SELECT", query="SELECT cur_cal FROM main_db WHERE user = %s AND keyword=%s ", val = (user,keyword))[0][0]
        cur_cal = str(cur_cal).replace('-','')
        if int(start_time) < int(cur_cal):
            start_time = cur_cal
        print(start_time)
        cal_list = self.date_out.cal(start_time, end_time)
        for cal in cal_list:
            self.db.keyword_get(type="UPDATE", query="UPDATE main_db SET cur_cal=%s WHERE user=%s AND keyword=%s;", val=(cal,user,keyword))
            for page in range(1,int(self.page)+1):
                #url + info
                url = "http://search.daum.net/search?w=news&sort=recency&q="+keyword + \
                      "&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p="+str(page)+"&rc=1&at=more&sd="+cal+"000000&ed="+cal+"235959&period=u"
                print(url)
                req = requests.get(url)
                soup = BeautifulSoup(req.text, "lxml")

                page = soup.find('span', id ='resultCntArea').text
                page = int(int(''.join(re.findall('\d', page.split('/')[1])))/10)

                if page <= self.page:
                    self.page = page
                else:
                    self.page = 250

                lists = soup.find_all('div','wrap_cont')
                for list in lists:
                    try:
                        title = list.find('a', 'f_link_b').text
                        href = list.find('a', 'f_link_b').get('href')
                        info = list.find('span', 'f_nb date').text
                        text = self.clean_text(info)
                        gisa_cal = text[0]
                        gisa_cal = self.date_out.ch_cal(gisa_cal)
                        writer = text[1:]
                        content = list.find('p', 'f_eb desc').text
                        words = self.kon.split_sen(content.encode('utf-8'))
                    except:
                        continue
                    news_dict = {"keyword":keyword, "title":title, "gisa_cal":gisa_cal, "writer":writer, "content":content, "href": href, "words" : words}

                    num += 1
                    gisa_list.append(news_dict)

                if not soup.find('div', 'paging_comm'):
                    break
                if len(lists) < 10:
                    break
                # #큐로 전달
                # qpublic.q_publish(json.dumps(news_dict))
                # print(json.dumps(news_dict))            

        return gisa_list

if __name__ == '__main__':
    page = '250'
    keyword = '트와이스'
    start_time = '20170101'
    end_time = '20180101'

    crawler = crawler(page)
    gisa_list = crawler.daum(keyword, start_time, end_time)
    print(gisa_list)

    for i in gisa_list:
        print(i['title'])