from typing import List
from pydantic import BaseModel
from entity.model import TrademarkItem


class SuggestResponse(BaseModel):
    productName: List[str] = []
    productNameEng: List[str] = []


class SearchResponse(BaseModel):
    total: int
    page: int
    size : int
    items: List[TrademarkItem]
