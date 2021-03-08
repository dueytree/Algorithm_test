# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

# 주어진 숫자 15를 연속된 자연수로 표현할 수 있는 모든 방법을 찾아야 한다.
# for문의 범위를 1부터 n+1까지 잡고, while문에 사용할 변수 way를 설정 한 뒤
# way가 n보다 작을 조건을 걸어준 다음, 반복해서 돌아가는 i를 way에 더해준 뒤 i를 +1해준다.
# while 조건에 way가 n보다 작을 때 반복문을 계속해서 돌리고, way가 n과 같을 때 answer값에 찾은 방법을 +1 해주고
# 계속 반복해서 진행 한 뒤 반복문이 끝나고 answer 값을 return한다.

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        way = 0
        while way < n:
            way += i
            i += 1
        if way == n:
            answer += 1
    return answer

print(solution(15))
def test_solution():
    assert solution(15) == 4