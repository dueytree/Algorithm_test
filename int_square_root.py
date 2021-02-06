# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

# n이 제곱수인지 확인하기 위해 변수 x에 n의 1/2값을 넣어주고 반복문으로 n의 제곱근을 구한다음
# 주어진 조건을 return하고, 제곱수가 아닐때 [-1]을 return 해주는 if문을 작성한다.
# # 오답
# def solution(n):
#     x = n * 0.5
#     for i in range(1, n):
#         if n == i ** 2:
#             return (i + 1) ** 2
#     if n != x ** 2:
#         return -1
#
# print(solution(121))
# print(solution(3))

# sqrt 함수를 사용하고, x가 양의 정수인 경우 x % 1 == 0 조건을 확인하여 해결

def solution(n):
    sqrt = n ** 0.5
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

print(solution(121))
print(solution(3))