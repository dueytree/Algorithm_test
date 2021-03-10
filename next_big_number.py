# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

# bin함수는 10진법을 2진법으로 바꿔주는 함수이다. 문제에서 n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같음으로
# bin함수를 사용해 2진법으로 변경하고, count함수를 통해 1의 갯수를 계산하고,
# for문을 통해 if조건문을 넣어 결과를 출력하는 방식으로 진행한다.
# 변수 bnry값에 n을 2진법으로 바꿔주고, 동시에 1의 갯수를 카운트로 지정하고,
# n이 1,000,000 이하 값으로 범위를 넣어주고 if 조건문에 i가 bnry값과 같을 때, return i를 해줘서 다음 큰 수를 구해준다.

def solution(n):
    bnry = bin(n).count('1')
    for i in range(n + 1, 1000001):
        if bin(i).count('1') == bnry:
            return i


def test_solution():
    assert solution(78) == 83
    assert solution(15) == 23