```md
# Trademark Search API

## 🚀 실행 방법

### 1. 설치

```bash
pip install -r requirements.txt
```

### 2. 실행

```bash
uvicorn main:app --reload
```

서버는 기본적으로 `http://127.0.0.1:8000`에서 실행됩니다.

---

## 📌 API 사용법

### 상표 검색 API

```
GET /trademarks/search
```

#### 사용예시

```
GET /trademarks/search?productName=프레스카&registerStatus=등록&page=0&size=20
```

#### ✅ 쿼리 파라미터

| 이름 | 타입 | 설명                             |
|------|------|--------------------------------|
| `productName` | string | 한글 상표명 (초성 검색 포함)              |
| `productNameEng` | string | 영문 상표명                         |
| `applicationNumber` | string | 출원번호                           |
| `applicationDateFrom` | date | 출원일 시작 범위                      |
| `applicationDateTo` | date | 출원일 끝 범위                       |
| `registerStatus` | enum | 등록 상태 (`등록`, `출원`, `거절`, `실효`) |
| `page` | int | 페이지 번호 (기본: 0)                 |
| `size` | int | 페이지당 항목 수 (기본: 10)             |

#### ✅ 응답 형식

```json
{
  "total": 1,
  "page": 0,
  "size": 20,
  "items": [
    {
      "productName": "프레스카",
      "productNameEng": "FRESCA",
      "applicationNumber": "4019950043843",
      "applicationDate": null,
      "registerStatus": "등록",
      ...
    }
  ]
}
```

---

### 자동완성 API

```
GET /trademarks/suggest
```

```
GET /trademarks/suggest?query=p
```

#### ✅ 응답 예시

```json
{
  "productName": [],
  "productNameEng": [
    "Penaten",
    "PICNIC",
    "pann",
    "PARKA CRYSTAL",
    "POCAHONTAS",
    "Paganini",
    "PASSION FIVE",
    "POZZO GELATERIA",
    "PROMINAR",
    "passion",
    "P SEOUL PALACE HOTEL",
    "PULMUONE",
    "PLANNING JAD",
    "PARABOLATUNE",
    "Phoenix Series"
  ]
}
```

---

## 구현된 기능 설명

- 초성 검색 (`ㅍㄹㅅㅋ` → `프레스카`)
- 한글/영문 상표명 필터링
- 등록 상태, 날짜 조건 필터링
- 자동완성 (한글/영문 분리)
- 페이지네이션 (`page`, `size` 쿼리)

---

## 기술적 의사결정

- **Controller-Service-Repository 구조**: 역할 분리로 유지보수성 향상
- **Jamo 라이브러리 사용**: 초성 검색 기능을 위한 한글 처리
- **자동완성 기능 도입**: 사용자의 검색 행동을 유도하고 만족도를 향상

---

## 고민한 점

- 초기에 하나의 파일에 로직을 몰아 작성하다가, 역할 분리를 고민하게 되었고 Controller, Service, Repository로 분리하게 되었습니다.
- 파일 기반이라 Repository가 실제 역할을 하기 어려워졌고, 필터링 로직이 몰리면서 다시 Service로 옮기게 되었습니다.
- 유틸성 함수들을 따로 `utils`로 뽑아내서 재사용성과 가독성을 높였습니다.
- 검색 기능의 본질은 “원하는 결과가 잘 나오는 것”이라는 점에 집중했습니다. 이를 위해 초성 검색, 자동완성 등을 추가했습니다.
- 자동완성 결과는 사용자의 혼용 검색 패턴에 대응하기 위해 사용자 입력에 따라 한글/영문을 구분해서 제공합니다.

---

## 개선하고 싶은 부분

- JSON 기반 데이터를 **PostgreSQL 등의 RDBMS로 이전**하여 구조 확장 예정
- 정밀한 검색 처리를 위해 **ElasticSearch와 병행 운용**할 수 있도록 설계
- 인기 키워드 기반 자동완성 정렬

---

## 📂 프로젝트 구조

```
.
├── main.py                  # FastAPI 진입점
├── controller/              # 라우터 정의
├── service/                 # 비즈니스 로직
├── repository/              # 데이터 접근
├── entity/
│   ├── model.py             # Pydantic 모델
│   ├── query.py             # request query
│   └── dto.py               # response dto 
├── utils/
│   └── text.py              # 정규화, 초성, 문자열 처리 유틸
└── data/
    └── trademark_sample.json
```

---

## 의존 라이브러리

- `fastapi`
- `uvicorn`
- `pydantic`
- `jamo`
```