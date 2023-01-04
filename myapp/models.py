from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id =  Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    is_active = Column(String)
    email = Column(String, unique=True, index=True)
    

class Blog(Base):
    __tablename__ = "Blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    article = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("Authors.id"))
    # owner = relationship("Author", back_populates="Blogs")
    
class category(Base):
    __tablename__ = "Blog_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
 

class Author(Base):
    __tablename__ = "Authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    mail = Column(String, index = True)
    hashed_password = Column(String)

    

