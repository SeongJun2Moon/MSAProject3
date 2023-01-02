school_drive = "C:/Users/MSJ/AIA/MsaProject/DjangoServer/exrc/webcrawler/webcrawler/chromedriver.exe"
home_drive = "C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/webcrawler/webcrawler/chromedriver.exe"
school_save = "C:/Users/MSJ/AIA/MsaProject/DjangoServer/exrc/webcrawler/save/naver.csv"
home_save = "C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/webcrawler/save/naver.csv"

import os
import platform
myos = platform.system()
root = r"C:\Users\MSJ\AIA\MsaProject\DjangoServer"
def dir_path(param):
    if (param == "algorithm"):
        return os.path.join(root, "util", param)
    elif (param == "buser") \
            or (param == "comments") \
            or (param == "posts") \
            or (param == "tags") \
            or (param == "views") :
        return os.path.join(root, "blog", param)
    elif (param == "fashion") \
            or (param == "fruits") \
            or (param == "iris") \
            or (param == "aitrader") \
            or (param == "number") :
        return os.path.join(root, "exrc", "dlearn", param)
    elif (param == "imdb") \
            or (param == "samsung_report") :
        return os.path.join(root, "exrc", "nlp", param)
    elif (param == "stroke") :
        return os.path.join(root, "exrc", param)
    elif (param == "webcrawler"):
        return os.path.join(root, "exrc", "webcrawler", param)
    elif (param == "cinema") \
             or (param == "movies") \
             or (param == "musers") \
             or (param == "showtimes") \
             or (param == "theater") \
             or (param == "theaterticket"):
        return os.path.join(root, "movies", param)
    elif (param == "users"):
        return os.path.join(root, "security", param)
    elif (param == "cart") \
             or (param == "categories") \
             or (param == "musers") \
             or (param == "deliveries") \
             or (param == "orders") \
             or (param == "products") \
             or (param == "susers"):
        return os.path.join(root, "shop", param)