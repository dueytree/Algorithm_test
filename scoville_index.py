# 더 맵
# https://programmers.co.kr/learn/courses/30/lessons/42626

# 주어진 문제는 heap을 사용하기를 원하는 문제이므로 heap에 대해 몰라서 구글링을 통해 공부했다.
# heap은 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조로
# 최대 힙, 최소 힙을 구하는 방식과 시간복잡도, 모듈 임포트와 heappush-pop-heapify를 공부해 사용했다.
# heapq는 push, pop을 적용할 때마다 정렬해주기 때문에 시간복잡도 관련 효율적이라고 한다.
# 우선 음식 횟수를 닮을 answer값을 정해주고, scoville 리스트를 heap으로 변환시켜준 뒤
# 스코빌 지수 기준의 k보다 scoville[0]값이 작을 때라는 조건을 걸어주고
# 스코빌 리스트 길이가 1과 같고 가장 앞 인덱스 값이 k보다 작을 때 더 이상 스코빌 지수를 k이상으로 만들 수 없기 때문에
# -1을 return해준다. 조건에 빠져나오게 되면 스코빌 지수 리스트에 가장 작은 지수와 그 다음 작은 지수를 뽑아 더해서
# 넣어준다. 그리고 횟수를 answer에 넣어주고 이 과정을 while조건이 충족될 때 까지 반복한다.



import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < k:
        if len(scoville) == 1 and scoville[0] < k:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer


def test_solution():
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2