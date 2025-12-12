import re

async def interpret_query(user_text: str) -> dict:
    user_text = user_text.lower()

    if "всего видео" in user_text:
        return {"operation":"count","table":"videos","filters":{}}

    if "видео у креатора" in user_text:
        creator_match = re.search(r"id\s*(\d+)", user_text)
        dates_match = re.search(r"с\s*(\d+)\s*\w+\s*(\d+)\s*по\s*(\d+)\s*\w+\s*(\d+)", user_text)
        filters = {}
        if creator_match:
            filters["creator_id"] = int(creator_match.group(1))
        if dates_match:
            filters["date_from"] = f"{dates_match.group(4)}-{dates_match.group(2).zfill(2)}-{dates_match.group(1).zfill(2)}"
            filters["date_to"] = f"{dates_match.group(4)}-{dates_match.group(4).zfill(2)}-{dates_match.group(3).zfill(2)}"
        return {"operation":"count","table":"videos","filters":filters}

    if "набрал" in user_text and "просмотров" in user_text:
        return {"operation":"count","table":"videos","filters":{"min_views":100000}}

    if "просмотров выросли" in user_text:
        date_match = re.search(r"(\d+)\s*\w+\s*(\d+)", user_text)
        filters = {}
        if date_match:
            filters["date"] = f"{date_match.group(2)}-{date_match.group(1).zfill(2)}"
        return {"operation":"sum_delta_views","table":"video_snapshots","filters":filters}

    if "разных видео получали новые просмотры" in user_text:
        date_match = re.search(r"(\d+)\s*\w+\s*(\d+)", user_text)
        filters = {}
        if date_match:
            filters["date"] = f"{date_match.group(2)}-{date_match.group(1).zfill(2)}"
        return {"operation":"count_distinct_snapshots_with_delta","table":"video_snapshots","filters":filters}

    return {"operation":"count","table":"videos","filters":{}}