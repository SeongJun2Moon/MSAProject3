import csv
import time
from os import path

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from exrc.nlp.imdb.models import Imdb_model
import numpy as np

from math import log, exp
from collections import defaultdict
from util.path import dir_path

class Imdb_service:
    def __init__(self):
        model = Imdb_model().create_rnn_model()

    def imdb_hook(self):
        model = Imdb_model()
        model.fit()


class NaverMovieService(object):
    def __init__(self):
        global url, driver_path, file_name, encoding, review_train, k
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page='
        driver_path = path.join(dir_path("webcrawler"), "chromedriver.exe")
        file_name = "C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/nlp/positivity/save/naver_movie_review_corpus.csv"
        review_train = "exrc/nlp/imdb/data/review_train.csv"
        encoding = "UTF-8"
        k = 0.5
        self.word_probs = []

    def process(self, new_review):
        self.model_fit()
        data = self.classify(new_review)
        return round(data*100)

    def crawling(self):
        if not path.exists(review_train):  # file_name -> review_train
            review_data = []
            driver = webdriver.Chrome(driver_path)
            for page in range(1, 2):
                driver.get(url + str(page))
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                all_tds = soup.find_all('td', attrs={'class', 'title'})
                for review in all_tds:
                    need_reviews_cnt = 1000
                    sentence = review.find("a", {"class": "report"}).get("onclick").split("', '")[2]
                    if sentence != "":  # 리뷰 내용이 비어있다면 데이터를 사용하지 않음
                        score = review.find("em").get_text()
                        review_data.append([sentence, int(score)])
            time.sleep(1)  # 다음 페이지를 조회하기 전 1초 시간 차를 두기
            with open(file_name, 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(review_data)
            driver.close()

        data = pd.read_csv(file_name, header=None)
        data.columns = ['review', 'score']
        result = [print(f"{i + 1}. {data['score'][i]}\n{data['review'][i]}\n") for i in range(len(data))]
        return result

    def load_corpus(self):
        corpus = pd.read_table(review_train, sep=",", encoding=encoding)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda : [0,0])
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts
    def isNumber(self, param):
        try:
            float(param)
            return True
        except ValueError:
            return False
    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1.0 - prob_if_class0)
                log_prob_if_class1 += log(1.0 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    def word_probablities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]
    def classify(self, doc):
        return self.probability(word_probs=self.word_probs, doc=doc)
    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밌네요': [1,0]
        '별로 재미없어요': [0,1]
        '''
        num_class0 = len([1 for _, point in train_X if point > 3.5])
        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        # print(f" ************  word_counts is {word_counts}")
        self.word_probs = self.word_probablities(word_counts, num_class0, num_class1, k)



if __name__ == '__main__':
    # service = Imdb_service()
    # service.imdb_hook()
    result = NaverMovieService().process('ㅗ')
    print(result)