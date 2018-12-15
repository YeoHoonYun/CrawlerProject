# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, date
import time,re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class date_out:
    def cal(self, start_date, end_date):
        start_cal = datetime.strptime(start_date,'%Y%m%d')
        end_cal = datetime.strptime(end_date,'%Y%m%d')
        cal_list = []

        while True:
            cal = start_cal.strftime('%Y%m%d')
            cal_list.append(cal)
            start_cal = start_cal + timedelta(days=1)


            if(start_cal > end_cal):
                break
        return cal_list

    def ch_cal(self, gisa_cal):
        now = time.strftime('%Y%m%d')
        if '분전' in gisa_cal:
            gisa_cal = (datetime.today() - timedelta(minutes=int(gisa_cal[:-2]))).strftime('%Y.%m.%d')
        elif '시간전' in gisa_cal:
            gisa_cal = (datetime.today() - timedelta(hours=int(gisa_cal[:-3]))).strftime('%Y.%m.%d')
        elif '일전' in gisa_cal:
            gisa_cal = (datetime.today() - timedelta(days=int(gisa_cal[:-2]))).strftime('%Y.%m.%d')
        elif '어제' in gisa_cal:
            gisa_cal = (datetime.today() - timedelta(days=1)).strftime('%Y.%m.%d')
        elif gisa_cal[-1] == '.':
            gisa_cal = gisa_cal[:-1]
        return gisa_cal

if __name__ == '__main__':
    date = date_out()
    print(date.cal(20161031,20161101))
