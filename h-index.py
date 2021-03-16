# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

# 논문 n 편 중, h번 이상 인용된 논문이 h편 이상일 때 h의 최댓값을 구하는 문제이다.
# 이하 인용된 논문에 신경쓸 필요없이 첫째로 인용 횟수 citations를 sort 정렬 해주고
# citations의 인덱스 길이를 length에 담아준 뒤 for문으로 인용 횟수만큼 돌고
# citations[i]값이 (length - i)보다 크거나 같을 때 (length - i)를 return 해주면 된다.
# 다 계산할 필요없이 최댓값만 뽑아내면 되는 문제기 때문에 sort 정렬 했기 때문에 끝까지 반복할 필요가 없다.
# 주의할 것은 테스트 케이스에 [0, 0, 0]과 같이 모든 인용 횟수가 0 일때 0으로 출력되지 않고 None으로 출력된다.

def solution(citations):
    citations.sort()
    length = len(citations)
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    # 모든 인용 횟수가 0 일때 None으로 출력되는 것을 방지.
    if sum(citations) == 0:
        return 0


def test_solution():
    assert solution([0, 0, 0]) == 0
    assert solution([3, 0, 6, 1, 5]) == 3
