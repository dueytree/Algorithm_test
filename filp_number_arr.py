# 자연수 뒤집어 배열로 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

# 정수값 n을 문자열로 바꿔주고 reversed 함수를 이용해 뒤집어 준다.
# for문으로 뒤집어준 문자열 만큼 돌고 돌때마다 그 값을 answer에 int 정수값으로 바꿔서 넣어준다.

def solution(n):
    answer = []
    str_n = reversed(str(n))
    for element in str_n:
        answer.append(int(element))
    return answer

print(solution(12345))