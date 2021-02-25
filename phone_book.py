import pytest

# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

# phone_book 배열에서 한 번호가 다른 번호의 접두어인지 확인하려면 들어있는지 확인하는 번호가 포함되어있는지 확인해야한다.
# 비교할 수를 임시변수에 설정해주고, for문으로 2번째 인덱스부터 포함되어있는지 조건을 걸어준다.
# 배열이 정렬되어 있지 않을 수 있기때문에 sort정렬해준다.

def solution(phone_book):
    phone_book.sort()
    target = phone_book[0]
    for i in range(1, len(phone_book)):
        if target in phone_book[i]:
            return False
    return True


def test_solution():
    assert solution(["119", "97674223", "1195524421"]) == False
    assert solution(["123", "456", "789"])
    assert solution(["12", "123", "1235", "567", "88"]) == False

