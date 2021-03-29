# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

# 첫 번째로 상하 조정으로 알파벳을 바꿔야 하기 때문에 각 알파벳마다 상하 조정 중에 min값으로 최소 횟수를 구해 담아두고
# i를 0부터 시작해서 좌우 이동 횟수를 answer에 더해 준다. 좌우 방향 전환 시에는 바꿔야하는 알파벳이 나오기까지의 좌우 횟수(거리)를
# 구하고, 그 중 최소값이 되는 방향으로 전환해준다. 모든 알파벳이 조정된 경우에(모든 방향을 계산, 반복한 후) 결과값을 반환한다.
# 이 문제는 ord, 아스키 코드 값을 돌려주는 내장 함수를 사용한다. 전에 배웠던 함수를 다시 찾아 공부한 후 적용했다.
# 조이스틱을 돌린다고 생각하고 가정하여 알파벳을 움직여 입력된 값을 최소로 구하는 문제인데, 탐욕법으로 문제를 풀이해야한다.

def solution(name):
    answer = 0
    i = 0
    stick = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    while True:
        answer += stick[i]
        stick[i] = 0
        if sum(stick) == 0:
            break
        left, right = 1, 1
        while stick[i - left] == 0:
            left += 1
        while stick[i + right] == 0:
            right += 1
        answer += left if left < right else right
        i += -left if left < right else right
    return answer

def test_solution():
    assert solution("JEROEN") == 56
    assert solution("JAN") == 23