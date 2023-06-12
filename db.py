from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://Akshpatel:Hello01234567!@localhost:5432/postgres"
#
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




class Books(Base): #sql insertion
    __tablename__ ="book"
    id=Column(int(20),unique=True)
    title=Column(String(50),unique=True)
    author=Column(String(50))
    publisher=Column(String(50)) //5
    Base.metadata.create_all(bind=engine)




app=FastAPI()
class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    class Config:
        orm_mode=True








@app.get("/user",response_model=list[Config])
def calling(book:Book):
    
    return f"(inserting:{book.author},)"


@app.post("/user")
def calling(book:Book):
    db = SessionLocal()
    new_book = Book(id=book.id, title=book.title, author=book.author, publisher=book.publisher)
    return new_book






