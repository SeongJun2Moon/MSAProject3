import csv
import os
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from webcrawler.models import Scrap


class ScrapServeice(Scrap):
    def __init__(self):
        global driverpath, naver_url, savepath, encoding
        driverpath = "./webcrawler/chromedriver.exe"
        savepath = "./webcrawler/save/naver.csv"
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        encoding = "UTF-8"

    def bugs_music(self, arg): # BeautifulSoup 기본 크롤링
        soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
        title = {"class": arg.class_names[0]}
        artist = {"class": arg.class_names[1]}
        titles = soup.find_all(name=arg.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv("result.csv")  # csv파일로 저장

    def melon_music(self, arg): # BeautifulSoup 기본 크롤링
        req = urllib.request.Request(arg.domain, headers=arg.headers)
        soup = BeautifulSoup(urlopen(req), arg.parser)
        _ = 0
        title = {"class": arg.class_names[0]}
        artist = {"class": arg.class_names[1]}
        titles = soup.find_all(name=arg.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=arg.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(1, len(titles) + 1), titles, artists)]
        diction = {}
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv("results.csv")

    def naver_movie_review(self):
        if os.path.isfile(savepath): # 파일유뮤 확인 코드
            naver_csv = pd.read_csv(savepath, header=None, index_col=0)
            naver_list = list(naver_csv.index)
            naver_json = [{"rank":i, "title":j} for i,j in enumerate(naver_list)]
            return naver_json
        else:
            driver = webdriver.Chrome(driverpath)
            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class': 'tit3'})
            products = [div.a.string for div in all_divs]
            print(products)
            df = pd.Series(products) # 리스트나 딕셔너리를 시리즈형식으로 출력
            print(type(df))
            df.index = df.index + 1
            print(df)
            df.to_csv(savepath, na_rep="NaN", header=None, index=None)
            driver.close()
            naver_csv = pd.read_csv(savepath, header=None, index_col=0)
            print(naver_csv.index)
            return naver_csv.index



if __name__ == '__main__':
    ScrapServeice().naver_movie_review()