# 수박 패턴
# https://programmers.co.kr/learn/courses/30/lessons/12922

# n의 홀수 짝수 여부에 따라 answer값에 수 와 박을 넣어주는 반복문을 사용

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

print(solution(3))
print(solution(4))