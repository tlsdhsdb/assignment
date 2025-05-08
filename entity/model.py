from typing import List, Optional
from pydantic import BaseModel,model_validator
from datetime import date
from enum import Enum

class RegisterStatus(str,Enum):
    등록 = "등록"
    출원 = "출원"
    실효 = "실효"
    거절 = "거절"


class TrademarkItem(BaseModel):
    productName: Optional[str]
    productNameEng: Optional[str]
    applicationNumber: str
    applicationDate: Optional[date]
    registerStatus: RegisterStatus
    publicationNumber: Optional[str]
    publicationDate: Optional[date]
    registrationNumber: Optional[List[Optional[str]]]
    registrationDate: Optional[List[Optional[date]]]
    registrationPubNumber: Optional[str]
    registrationPubDate: Optional[str]
    internationalRegDate: Optional[str]
    internationalRegNumbers: Optional[str]
    priorityClaimNumList: Optional[List[str]] = None
    priorityClaimDateList: Optional[List[Optional[date]]]
    asignProductMainCodeList: Optional[List[Optional[str]]]
    asignProductSubCodeList: Optional[List[Optional[str]]]
    viennaCodeList: Optional[List[Optional[str]]]

    @model_validator(mode="before")
    @classmethod
    def parse_dates(cls, values):
        # 직접 필드를 수정
        def parse_yyyymmdd(v):  # 내부 함수로 정의
            if isinstance(v, str) and len(v) == 8:
                try:
                    return date.strptime(v, "%Y%m%d").date()
                except:
                    return None
            return v

        for key in ["applicationDate", "publicationDate", "registrationPubDate", "internationalRegDate"]:
            if key in values:
                values[key] = parse_yyyymmdd(values[key])

        if "priorityClaimDateList" in values and values["priorityClaimDateList"]:
            values["priorityClaimDateList"] = [parse_yyyymmdd(v) for v in values["priorityClaimDateList"]]

        if "registrationDate" in values and values["registrationDate"]:
            values["registrationDate"] = [parse_yyyymmdd(v) for v in values["registrationDate"]]

        return values

