# JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

# 빈 문자열 answer와 문자열 s의 공백을 제외하고 대소문자 처리를 진행해줄 count를 변수로 설정하고
# s 길이만큼 for문을 돌려 i가 공백일시에 count를 i + 1처리를 해줘서 공백을 지나치고 다음번 문자로 넘어갈수 있게
# 조건을 걸어준다. elif로 i + 1을 넣어준 count와 i를 비교해 가장 첫자리는 upper함수로 대문자를 출력하고
# else로 나머지 소문자를 출력해준다.

import pytest
def solution(s):
    answer, count = '', 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            count = i + 1
        elif i == count:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

def test_solution():
    assert solution("3people unFollowed me") == "3people Unfollowed Me"
    assert solution("for the last week") == "For The Last Week"
