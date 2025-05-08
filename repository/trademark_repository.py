# repositories/trademark_repository.py
import json
from entity.model import TrademarkItem
from functools import lru_cache


@lru_cache()
def load_data():
    with open("data/trademark_sample.json", encoding="utf-8") as f:
        raw = json.load(f)
    return [TrademarkItem(**r) for r in raw]

