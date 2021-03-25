# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

# 문제를 잘 읽어보면 생각보다 간단하게 풀 수 있다. 문제에서 제시한대로, 참가자들의 경기는 리그 형식이 아니라
# 토너먼트 형식이다. 두 참가자 중 한 참가자 만이 다음 라운드에 진출하고, 그 전체 참가자 중 a와 b의 경기가
# 몇 번째 라운드에서 만나는지 구하는 문제이다. a, b는 서로 만나기 전까지 항상 승리해서 무조건 다음 라운드 진출을
# 전제로 하기 때문에 a와 b의 참가번호를 비교하여 경우를 끝까지 반복하고 a, b가 다음 라운드에 진출할 때,
# 참가번호를 새로 받을 식을 넣어 계산 해주면 된다. 라운드가 끝날 때 answer 값을 +1을 증가 시켜준다.

def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    return answer

def test_solution():
    assert solution(8, 4, 7) == 3