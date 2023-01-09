from sqlalchemy.orm import Session

from app.database import engine, conn
from app.models.post import Post
import pymysql
from sqlalchemy.orm import sessionmaker
pymysql.install_as_MySQLdb()

def find_posts_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()

def find_posts(db: Session):
    # Session = sessionmaker(bind=engine)
    # session = Session()
    return db.query(Post).all()