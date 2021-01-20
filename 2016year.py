# 문제 설명
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.
#
# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
#
# 입출력 예
# a	b	result
# 5	24	TUE


# 달과 일수, 요일을 리스트에 넣고 반복문을 돌려 해당 달과 일수의 반복에 따라 요일값이 나오도록 진행

# def solution(a, b):
#     month = 12
#     day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     day_of_the_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
#
#     for i in range(month):
#         count = 0
#         if i == a:
#             i = a
#         for j in range(day[a - 1]):
#             if j == b:
#                 j = b답
#                 count = sum(day[:i]) + j
#                 count = count // len(day_of_the_week) - 1
#                 return day_of_the_week[count]
#
# print(solution(5, 24))

## 정답
from datetime import date
def solution(a, b):
    return date(2016,a,b).strftime('%a').upper()

print(solution(12, 31))