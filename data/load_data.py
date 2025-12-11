import os
import json

from database.models.snapshot_model import Snapshot
from database.models.video_model import Video
from database.session import SessionLocal

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "videos.json")

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

def load(json_data):
    db = SessionLocal()
    try:
        for video in json_data['videos']:
            new_video = Video(
                id=video['id'],
                video_created_at=video['video_created_at'],
                views_count=video['views_count'],
                likes_count=video['likes_count'],
                reports_count=video['reports_count'],
                comments_count=video['comments_count'],
                creator_id=video['creator_id'],
                created_at=video['created_at'],
                updated_at=video['updated_at']
            )
            db.add(new_video)

            for snapshot in video.get('snapshots', []):
                new_snapshot = Snapshot(
                    id=snapshot['id'],
                    video_id=snapshot['video_id'],
                    views_count=snapshot['views_count'],
                    likes_count=snapshot['likes_count'],
                    reports_count=snapshot['reports_count'],
                    comments_count=snapshot['comments_count'],
                    delta_views_count=snapshot['delta_views_count'],
                    delta_likes_count=snapshot['delta_likes_count'],
                    delta_reports_count=snapshot['delta_reports_count'],
                    delta_comments_count=snapshot['delta_comments_count'],
                    created_at=snapshot['created_at'],
                    updated_at=snapshot['updated_at']
                )
                db.add(new_snapshot)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    load(data)