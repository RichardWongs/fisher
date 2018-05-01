from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    author = Column(String(30),default='未名')
    binding = Column(String(20))    #装帧版本
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))    #出版日期
    isbn = Column(String(15),nullable=False,unique=True)
    summary = Column(String(1000))  #简介
    image = Column(String(50))

    # def __init__(self,title,author):
    #     self.title = title
    #     self.author = author
    #
    # def __repr__(self):
    #     return '<Book %r,%r>' % self.title,self.author