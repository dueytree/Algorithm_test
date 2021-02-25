# 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

# 문자열의 숫자중 최소값과 최대값을 찾아야 한다. 일단 주어진 숫자들이 문자열로 묶여있기때문에
# split을 사용해 나눠주고, map과 list로 덮어 정수형으로, 리스트로 묶여나오는 값을 임시리스트 변수에 넣어준 뒤,
# max, min을 활용해 최대 최소값을 구해준다.
# 마지막으로 answer값에 문자열 최소값과 최대값을 넣어준 뒤, return값에 나오는 숫자들에 공백이 한칸 있으므로 그 공백을 중간에 넣어준다.

import pytest

def solution(s):
    check_list = list(map(int, s.split(' ')))
    max_num, min_num = max(check_list), min(check_list)
    answer = str(min_num) + " " + str(max_num)
    return answer



def test_solution():
    assert solution("1 2 3 4") == "1 4"
    assert solution("-1 -2 -3 -4") == "-4 -1"
    assert solution("-1 -1") == "-1 -1"

