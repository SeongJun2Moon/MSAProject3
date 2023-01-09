from sqlalchemy.orm import Session


from app.models.user import User, Post


def find_users(db: Session):
    return db.query(User).all()

def find_posts(db : Session):
    return db.query(Post).all()