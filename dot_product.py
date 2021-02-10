# 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

# 주어진 a와 b 리스트 각각 index에 대응하는 수들을 곱해준다음, 이 수를 모두 더해주는 방식

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))