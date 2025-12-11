from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.session import Base

class Snapshot(Base):
    __tablename__ = "snapshots"

    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    views_count = Column(Integer)
    likes_count = Column(Integer)
    comments_count = Column(Integer)
    reports_count = Column(Integer)
    delta_views_count = Column(Integer)
    delta_likes_count = Column(Integer)
    delta_comments_count = Column(Integer)
    delta_reports_count = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    video = relationship("Video", back_populates="snapshots")