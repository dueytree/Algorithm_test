# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048

# 이 문제는 일정한 규칙이 존재한다. 문제를 자세히 보면 그림을 옆으로 뒤집으면 좌표처럼 확인할 수 있다.
# 높이 3 가로 2 일때 꼭지점에서 만나고, 6, 4 일때 9, 6 일때 만난다.
# 가로의 길이는 2의 배수로, 세로는 3의 배수로 지점을 지난다. 첫번째 답은 가로와 세로의 길이의 최대공약수를 각각 for문으로
# 임시 리스트를 정해 append 해주고, 마지막 set과 intersection으로 교집합을 구해 최대공약수를 구하는 방식으로 풀었으나
# 시간복잡도 시간초과로 오답처리 되었다. 예전 문제에서 다루고 배웠던 gcd, lcm을 참고해 다시 풀었다.
# math를 import하고, 가로와 세로의 최대공약수를 구해주는 식을 써준 다음, 그 식을 gcd_ 변수에 넣어준 뒤
# 가로 세로 전체 길이의 사각형에서 가로 세로 더한 값과 최대공약수를 제거해준 값을 빼서 나온 값을 return했다.
# 시간복잡도 차이가 굉장히 크다.


# # 첫번째 답
# def solution(w, h):
#     w_list = []
#     h_list = []
#     for i in range(1, w + 1):
#         if w % i == 0:
#             w_list.append(i)
#     for j in range(1, h + 1):
#         if h % j == 0:
#             h_list.append(j)
#     answer = set(w_list).intersection(h_list)
#     return w * h - (w + h - max(answer))


import math

def solution(w, h):
    gcd_ = math.gcd(w, h)
    return w * h - (w + h - gcd_)




def test_solution():
    assert solution(8, 12) == 80