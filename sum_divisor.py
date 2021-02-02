# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

# n의 범위만큼 반복문을 돌려 n을 i로 나눠 0으로 떨어질때 answer에 값을
# 더해주는 방식

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

print(solution(12))
print(solution(5))