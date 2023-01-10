from sqlalchemy.orm import Session

from app.database import conn
from app.models.post import Post
import pymysql

pymysql.install_as_MySQLdb()

def find_posts_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_posts(db: Session):
    return db.query(Post).all()