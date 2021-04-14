# 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907

# 일단 문제 조건이 n가격에서 money 리스트에 담긴 동전으로 몇 가지 방법으로 지불할 수 있는지 찾는 것이다.
# money 리스트를 반복문으로 돌며 지금 현재 선택한 동전으로 n원 이하까지의 금액을 만들 수 있는 경우의 수를 answer 리스트에 넣는다.
# 만들어서 비교해야할 금액이 선택한 동전보다 작은 경우는 없으니까 price range는 (coin, n + 1)로 한다.
# 그리고 조건문으로 price와 coin의 비교를 만들어 주고 answer[price]에 answer[price - coin] 값을 더해준다.
# price - coin 값을 더해주는 것은 만들 수 있는 경우에 coin을 붙여준게 answer[price]가 되기 때문.

def solution(n, money):
    answer = [1] + [0] * n
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                answer[price] += answer[price - coin]
    return answer[n] % 1000000007

def test_solution():
    assert solution(5, [1, 2, 5]) == 4
