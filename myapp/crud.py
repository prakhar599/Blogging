from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_Author(db: Session, author: schemas.AuthorSchema):
    db_author = models.Author(first_name=author.first_name,last_name = author.last_name,mail = author.mail, hashed_password=author.hashed_password)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def get_Blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def del_Blogs(db: Session,blog_id:int):
    db.query(models.Blog).filter(models.Blog.id == blog_id).delete()
    db.commit()
    return {"msg":"Item deleted successfully"}

def create_author_Blog(db: Session, Blog: schemas.BlogSchema, author_id: int):
    db_item = models.Blog(**Blog.dict(),author_id=author_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_cats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.category).offset(skip).limit(limit).all()


def create_cat(db: Session, item : schemas.CatSchema):
    db_item = models.category(name= item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
