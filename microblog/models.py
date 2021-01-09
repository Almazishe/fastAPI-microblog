from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from user.models import User

from core.db import Base



class Post(Base):
    __tablename__ = 'microplog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)