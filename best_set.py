# 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938

# 일단 조건대로 자연수 갯수 n이 s보다 작은 것은 불가능하다. 따라서 n이 s보다 큰 경우는 [-1]을 리턴해준다.
# 그리고 숫자 s를 자연수 n개로 표현하면서 곱이 가장 큰 수가 되도록 하려면 n의 자연수 사이 차이가 적어야 곱이 커질 수 있다.
# 숫자 s를 n으로 나눈 값을 answer 리스트에 저장하면 일단 곱이 가장 큰 조합이 만들어진다.
# s를 n으로 나눈 나머지가 남을 수 있는데, 이럴 땐 오름차순 정렬을 맞춰야하기 때문에 리스트 맨 뒤에서부터 더해줘야
# 오름차순 정렬을 지킬 수 있다.
# [-1]을 return해주는 조건문을 정하고, s를 n으로 나눈 값이 n개가 되도록 초기값 설정을 진행한다.
# 이후 s를 n으로 나눈 값에서 나머지만큼 각 인덱스 값에 1씩 더해준다. 그리고 저장된 answer를 return한다.


def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    tmp = s // n
    for _ in range(n):
        answer.append(tmp)
    idx = len(answer) - 1
    for _ in range(s % n):
        answer[idx] += 1
        idx -= 1
    return answer


def test_solution():
    assert solution(2, 9) == [4, 5]
    assert solution(2, 1) == [-1]
    assert solution(2, 8) == [4, 4]