from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

from database.session import Base

class Video(Base):
    __tablename__ = 'videos'
    id = Column(String, primary_key=True)
    creator_id = Column(String)
    video_created_at = Column(DateTime)
    views_count = Column(Integer)
    likes_count = Column(Integer)
    comments_count = Column(Integer)
    reports_count = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    snapshots = relationship("Snapshot", back_populates="videos")