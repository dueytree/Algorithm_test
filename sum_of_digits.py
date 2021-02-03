# 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

# 재귀함수를 사용해서 10의 단위로 나눠 각 자리수를 구하고, 다시 solution 함수 n값을 10으로 나머지 제하고 나눈 값을
# 다시 더해주면서 10보다 작을때는 n을 리턴해 함수를 종료시킨다.
def solution(n):
    if n < 10:
        return n
    return n % 10 + solution(n // 10)


print(solution(123))
print(solution(987))