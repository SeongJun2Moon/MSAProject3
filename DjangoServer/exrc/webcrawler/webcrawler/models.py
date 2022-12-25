

import pandas as pd

from isort._future._dataclasses import dataclass


context = 'C:/Users/SJMoon/AIA/MSAProject/DjangoServer/webcrawler/'


@dataclass
class Scrap:
    html = ""
    parser = ""
    domain = ""
    query_string = ""
    headers = {}
    tag_name = ""
    fname = ""
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.diction, orient='index') #orient='index'는 index를 자동 선언