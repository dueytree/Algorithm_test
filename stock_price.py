# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

# 리스트 prices에 deque를 사용해 덮어주고, prices값을 모두 반복하는 while문을 작성한다.
# 그 안에 임시변수 value, prices의 가장 맨 앞을 제거해주는 값과 가격이 떨어지지 않은 초를 나타내는 count값을 지정한다.
# 그리고 for문으로 prices의 element값을 돌고, if문으로 element 값이 감소하는 경우라면 count에 += 1을 추가해준다음 반복문을 끝내고,
# 아닐시에 for문을 빠져나온상태에서 초값 count를 += 1 해준다. 그리고 answer값에 구하고자 하는 초 값을 append해주고 return한다.

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        value = prices.popleft()
        cnt = 0
        for element in prices:
            if value > element:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3]))