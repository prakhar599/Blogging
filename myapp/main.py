from fastapi import Depends, FastAPI, HTTPException,Body
from sqlalchemy.orm import Session
from myapp.auth_bearer import JWTBearer
from . import crud, models, schemas
from .database import SessionLocal, engine
from uuid import uuid4
from myapp.auth_handler import signJWT
from myapp.schemas import UserSchema, AuthorLoginSchema, AuthorSchema, UserLoginSchema, CatSchema,BlogSchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
        
        
@app.get("/")
def home():
    return "A Simple Blogging Api"        

@app.post("/author/signup", tags=["Author"])
def create_author(db: Session = Depends(get_db),author: AuthorSchema = Body(...)):
    crud.create_Author(db,author=author)
    return signJWT(author.mail)

@app.post("/author/login", tags=["Author"]) 
def read_author(author: AuthorLoginSchema = Body(...),db: Session=Depends(get_db)):
    authors = crud.get_authors(db)
    for ppl in authors:
        if ppl.mail == author.mail and ppl.hashed_password == author.hashed_password:
            return signJWT(ppl.mail)
    return { "error": "Wrong login details!"} 


@app.post("/author/{author_id}/Blogs/", tags=["Blogs"]) #dependencies=[Depends(JWTBearer())],response_model=schemas.BlogSchema,
def create_Blog_for_author(
    author_id: int, Blog: schemas.BlogSchema, db: Session = Depends(get_db)
):
    return crud.create_author_Blog(db=db, Blog=Blog, author_id=author_id)


@app.delete("/blog/{blog_id}/del", tags=["Blogs"])
def del_cat(blog_id:int ,db: Session = Depends(get_db)):
    return crud.del_Blogs(db,blog_id=blog_id)

    
@app.post("/cat", dependencies=[Depends(JWTBearer())], tags=["Category"])
def create_cat(db: Session = Depends(get_db),item: CatSchema = Body(...)):
    return crud.create_cat(db,item=item)

@app.get("/cats/", tags=["Category"])
def read_cats(skip: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    return crud.get_cats(db, skip=skip, limit=limit)
       

@app.get("/authors/", tags=["Author"]) #response_model=list[schemas.BlogSchema],
def read_Authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Authors = crud.get_authors(db, skip=skip, limit=limit)
    return Authors


@app.get("/Blogs/", tags=["Blogs"]) #response_model=list[schemas.BlogSchema],
def read_Blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Blogs = crud.get_Blogs(db, skip=skip, limit=limit)
    return Blogs


@app.post("/user/signup", tags=["User"])
def create_user(db: Session = Depends(get_db),user: UserSchema = Body(...)):
    crud.create_user(db,user=user)
    return signJWT(user.email)

@app.get("/users/", tags=["User"]) #response_model=list[schemas.BlogSchema],
def read_Users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Users = crud.get_users(db, skip=skip, limit=limit)
    return Users

