from sqlalchemy import Column, Integer, DateTime

from database.session import Base

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    creator_id = Column(Integer)
    video_created_at = Column(DateTime)
    views_count = Column(Integer)
    likes_count = Column(Integer)
    comments_count = Column(Integer)
    reports_count = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
