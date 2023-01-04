from pydantic import BaseModel,  Field, EmailStr

    
class BlogSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    article: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "article": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens....",
            }
        }


class UserSchema(BaseModel):
    email: EmailStr = Field(...)
    hashed_password: str = Field(...)  
    is_active : bool = Field(...)
    id : int = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "hashed_password": "any",
                "is_active": "true"
            }
        }
        
 
 
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    hashed_password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.comm",
                "hashed_password": "any"
            }
        }     
              


class AuthorSchema(BaseModel):
    first_name : str = Field(...)
    last_name : str = Field(...)
    mail : str = Field(...)
    hashed_password: str = Field(...)  
    id : int = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "SitaRam",
                "last_name": "Goyel",
                "hashed_password": "any",
                "mail": "sitaram@gmail.com"
            }
        }
        
class AuthorLoginSchema(BaseModel):
    mail: EmailStr = Field(...)
    hashed_password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "mail": "sitaram@gmail.com",
                "hashed_password": "any"
            }
        }     
       

           
class CatSchema(BaseModel):
    name :  str = Field(...)
    id : int = Field(default=None)

    class Config:
        schema_extra = {
            "example": {    
                "name": "HIQ"
            }
        } 
                      
        
        
        
