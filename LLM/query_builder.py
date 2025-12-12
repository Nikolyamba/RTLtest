from typing import Dict

def build_where(filters: Dict):
    parts = []
    if not filters:
        return ""

    if "creator_id" in filters:
        parts.append(f"creator_id = {int(filters['creator_id'])}")

    if "date_from" in filters and "date_to" in filters:
        parts.append(f"video_created_at::date BETWEEN '{filters['date_from']}' AND '{filters['date_to']}'")

    if "date" in filters:
        parts.append(f"created_at::date = '{filters['date']}'")

    if "min_views" in filters:
        parts.append(f"views_count >= {int(filters['min_views'])}")

    if parts:
        return "WHERE " + " AND ".join(parts)
    return ""

def build_sql(data: Dict) -> str:
    op = data.get("operation")
    table = data.get("table")
    filters = data.get("filters", {})

    where = build_where(filters)

    if op == "count" and table in ("videos", "video_snapshots"):
        return f"SELECT COUNT(*) FROM {table} {where};"

    if op == "sum_delta_views":
        return f"SELECT COALESCE(SUM(delta_views_count),0) FROM video_snapshots {where};"

    if op == "count_distinct_snapshots_with_delta":
        w = where
        if w:
            w = w.replace("WHERE ", "")
            return f"SELECT COUNT(DISTINCT video_id) FROM video_snapshots WHERE delta_views_count > 0 AND {w};"
        return "SELECT COUNT(DISTINCT video_id) FROM video_snapshots WHERE delta_views_count > 0;"

    raise ValueError(f"Unknown operation: {op}")