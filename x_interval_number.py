# x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954

# 반복문을 숫자 n의 범위 만큼 돌리고, answer 리스트에 x범위를 계산해 구한 숫자를 넣어준다.

def solution(x, n):
    answer = []
    for i in range(n) :
        answer.append(x * (i + 1))
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))