# 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

# if문으로 짝수를 고르는 조건을 걸어 간단하게 해결

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(solution(3))
print(solution(4))