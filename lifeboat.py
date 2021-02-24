# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

# 다리 지나가는 문제와 비슷하다. 모든 전개 과정을 다 돌아야 한다.
# 무게 한계가 존재하는데, 무게에 맞게 두명의 사람이 동시에 보트를 탈수 있기때문에 최소한의 보트운행을 진행하려면
# 주어진 people 리스트를 정렬 해주고, 첫 사람부터 끝 사람까지의 변수를 지정하고 while문을 통해 사람들의 몸무게 limit 조건을
# 걸어준다.

def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    answer = 0
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))