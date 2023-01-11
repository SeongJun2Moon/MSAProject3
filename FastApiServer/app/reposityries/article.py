from app.models.article import Article
import pymysql
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()

#
# def find_articles_legacy():
#     cursor = conn.cursor()
#     sql = "select * from posts"
#     cursor.execute(sql)
#     return cursor.fetchall()


def find_articles(page: int, db: Session):
    print(page)
    return db.query(Article).all()

