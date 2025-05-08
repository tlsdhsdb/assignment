from typing import Optional
from pydantic import BaseModel
from entity.model import RegisterStatus
from datetime import date


class TrademarkSearchQuery(BaseModel):
    applicationNumber: Optional[str] = None
    productName: Optional[str] = None
    productNameEng: Optional[str] = None
    applicationDateFrom: Optional[date] = None
    applicationDateTo: Optional[date] = None
    registerStatus: Optional[RegisterStatus] = None
