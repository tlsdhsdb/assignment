# utils/text.py
import re
from jamo import h2j, j2hcj

CHOSUNG = {'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
           'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'}

def normalize(text: str) -> str:
    return re.sub(r"[^가-힣a-zA-Z0-9]", "", text.lower())

def is_chosung_only(text: str) -> bool:
    return all(ch in CHOSUNG for ch in text)

def get_chosung_jamo(text: str) -> str:
    return ''.join(j2hcj(h2j(ch))[0] for ch in text if h2j(ch))

def match_chosung_jamo(user_input: str, text: str) -> bool:
    return user_input in get_chosung_jamo(text)

def is_korean(text: str) -> bool:
    return any('가' <= ch <= '힣' for ch in text)

def is_english(text: str) -> bool:
    return any('a' <= ch.lower() <= 'z' for ch in text)