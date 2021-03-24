# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

# 이번 문제는 위장할 때 입거나 사용할 물품을 매일 다른 조합으로 사용하도록 하는 문제이다.
# 출제 의도가 해시로 문제를 풀도록 하게끔 해서 해시를 다시 찾아보고 딕셔너리를 이용해 문제를 풀었다.
# 입을 옷을 담아 둘 dictionary를 items에 지정하고, 최소 한개 이상이고, 조합의 수를 계산할 때 곱셈을 사용하기 때문에
# answer값을 1로 지정한다. 입력받은 clothes를 돌면서 items의 두번째 옷의 종류가 dictionary안에 있는지
# 확인하고 있으면 items 옷의 종류값으로 옷의 이름 list를 가져와서 append해주고, 만약 없을 시에 value값에 옷의 이름을 추가한다.
# items반복문을 설정하고 옷의 종류값에 해당하는 list의 길이에 +1 해준다음 *= 해준다. 안입는 경우도 있기 때문에,
# 마지막에 둘다 안입는 경우는 제외하기 위해 answer -1 해준다.

def solution(clothes):
    answer = 1
    items = {}
    for element in clothes:
        if element[1] in items:
            items[element[1]].append(element[0])
        else:
            items[element[1]] = [element[0]]
    for tmp in items:
        answer *= len(items[tmp]) + 1
    return answer - 1


def test_solution():
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) == 3