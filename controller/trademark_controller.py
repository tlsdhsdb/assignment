from typing import List

from fastapi import APIRouter, Depends, Query
from entity.query import TrademarkSearchQuery
from entity.dto import SuggestResponse,SearchResponse
from service.trademark_service import search_trademarks, suggest_keyword

router = APIRouter()


@router.get("/search", response_model=SearchResponse)
def search(query: TrademarkSearchQuery = Depends(), page: int = Query(0, ge=0), size: int = Query(10, ge=1, le=100)):
    return search_trademarks(query, page, size)


@router.get("/suggest", response_model=SuggestResponse)
def autocomplete(query: str):
    return suggest_keyword(query)
