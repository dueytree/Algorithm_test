# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

# n까지의 수를 반복하며 n, m의 최대공약수를 구하고, 두 수의 최대공약수가 1일때 최소공배수로 두 수를 곱해주고
# 아닐 때 일반적인 최소공배수 구하는 공식을 사용한다.

def solution(n, m):
    for i in range(1, n + 1):
        if n % i == 0 and m % i == 0:
                tmp = i
    if tmp == 1:
        val = n * m
    else:
        val = tmp * (n // tmp) * (m // tmp)
    return [tmp, val]

print(solution(3, 12))
print(solution(2, 5))