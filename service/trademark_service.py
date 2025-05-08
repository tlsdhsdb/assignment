# services/trademark_service.py

from entity.query import TrademarkSearchQuery
from entity.dto import SuggestResponse,SearchResponse
from repository.trademark_repository import load_data
from util.text import is_chosung_only, normalize, match_chosung_jamo, is_korean, is_english

def search_trademarks(query: TrademarkSearchQuery,page: int = 0, size: int = 10) -> SearchResponse:
    data = load_data()

    if query.applicationNumber:
        data = [d for d in data if d.applicationNumber == query.applicationNumber]

    if query.productName:
        keyword = normalize(query.productName)
        if is_chosung_only(keyword):
            data = [d for d in data if d.productName and match_chosung_jamo(keyword, d.productName)]
        else:
            data = [d for d in data if d.productName and keyword in normalize(d.productName)]

    if query.productNameEng:
        keyword = normalize(query.productNameEng)
        data = [d for d in data if d.productNameEng and keyword in normalize(d.productNameEng)]

    if query.applicationDateFrom:
        data = [d for d in data if d.applicationDate and d.applicationDate >= query.applicationDateFrom]
    if query.applicationDateTo:
        data = [d for d in data if d.applicationDate and d.applicationDate <= query.applicationDateTo]

    if query.registerStatus:
        data = [d for d in data if d.registerStatus == query.registerStatus]

    return SearchResponse(
        total = len(data),
        page = page,
        size = size,
        items = data[page: page + size]
    )



def suggest_keyword(q: str) -> SuggestResponse:
    data = load_data()
    keyword = normalize(q)

    korean = set()
    english = set()

    if is_chosung_only(keyword):
        korean.update(
            d.productName for d in data if d.productName and match_chosung_jamo(keyword, d.productName)
        )
    elif is_korean(keyword):
        korean.update(
            d.productName for d in data if d.productName and normalize(d.productName).startswith(keyword)
        )
    elif is_english(keyword):
        english.update(
            d.productNameEng for d in data if d.productNameEng and normalize(d.productNameEng).startswith(keyword)
        )

    return SuggestResponse(productName=list(korean), productNameEng=list(english))