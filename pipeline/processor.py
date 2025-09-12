from typing import List, Dict

def validate_post(record: Dict) -> bool:
    # simple validation
    required = ("userId", "id", "title", "body")
    return all(k in record for k in required)

def transform_post(record: Dict) -> Dict:
    # normalize keys and convert types
    return {
        "post_id": int(record.get("id")),
        "user_id": int(record.get("userId")),
        "title": record.get("title", "")[:255],
        "body": record.get("body", ""),
    }

def process_batch(records: List[Dict]) -> List[Dict]:
    out = []
    for r in records:
        if not validate_post(r):
            continue
        out.append(transform_post(r))
    return out
