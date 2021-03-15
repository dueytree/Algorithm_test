# 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

# 피보나치 수열을 활용해 계산한다. 예시된 f(2) 식을 참고해 num변수에 [0, 1]을 넣어주고, n - 1 범위만큼 for문을 쓰고
# num 리스트에 f[0] + f[1] 값을 append 해준다. 반복문이 끝나면 return num[-1(마지막값] % 1234567을 써준다.

def solution(n):
    num = [0, 1]
    for i in range(n - 1):
        num.append(num[-2] + num[-1])
    return num[-1] % 1234567


def test_solution():
    assert solution(3) == 2
    assert solution(5) == 5