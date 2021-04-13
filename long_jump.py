# 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914

# 규칙을 보면 효진이는 한번 뛸 때 마다 1, 2칸씩만 뛸 수 있다.
# 1칸씩 뛰는 것부터 2번씩 뛰는 것까지 처음부터 끝까지 한번씩 비교하게 되면
# 뛰어야하는 길이와 몇 가지 방법이 있는지 구할 수 있다. 이 규칙을 찾으면 기본 피보나치 수열 방식과
# 비슷하다는 것을 알 수 있다.
# answer에 효진이가 한번 뛸 수 있는 거리 1, 2를 리스트로 넣어주고
# 뛸 수 있는 거리의 총 수가 3이기 때문에 조건문 설정을 해준 뒤
# 최대로 뛸 수 있는 거리 2와 n의 범위를 정해준 뒤 피보나치 수열 식을 넣어서 answer에 값을 append해준다.
# 마지막엔 문제 조건대로 1234567 나눈 나머지를 계산해 return 해준다.

def solution(n):
    answer = [1, 2]
    if n < 3:
        return n
    for i in range(2, n):
        answer.append(answer[i - 1] + answer[i - 2])
    return answer[-1] % 1234567

def test_solution():
    assert solution(4) == 5
    assert solution(3) == 3