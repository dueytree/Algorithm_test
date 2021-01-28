# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 소수의 갯수를 담는 count변수와 소수를 판별할때 사용할 tmp변수를 지정하고
# for문을 1부터 입력받은 n사이의 정수중에서 그보다 작은 수로 나누었을때 나눠 떨어지면
# tmp를 증가시키고 이때 나눠진 값이 없어 count값이 0일때 count 값에 + 1 해준다.

# 나의 풀이, 시간초과
# def solution(n):
#     count = 0
#     tmp = 0
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 tmp += 1
#         if tmp == 0:
#             count += 1
#         tmp = 0
#     return count
#
# print(solution(10))
# print(solution(5))


# 다른 해설
def solution(n):
    n += 1
    answer = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if answer[i] == True:
            for j in range(i + i, n, i):
                answer[j] = False
    a = [i for i in range(2, n) if answer[i] == True]
    return len(a)

print(solution(10))
print(solution(5))