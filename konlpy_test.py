# -*- coding: utf-8 -*-
from konlpy.tag import Kkma
from konlpy.utils import pprint

# pprint(self.kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
# word = self.kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^')

class konlpy_test:
    def __init__(self):
        self.kkma = Kkma()

    def split_sen(self, text):
        words = [x[0] for x in self.kkma.pos(text) if x[1] == 'NNG']
        return words

if __name__ == '__main__':
    kon = konlpy_test()
    text = u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'
    works = kon.split_sen(text)
    print(works)