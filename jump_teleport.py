# 점프와 순간이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

# 단순하게 점프는 에너지가 들고 순간이동은 에너지 소모없이 사용할 수 있다.
# 순간이동을 사용하려면 현재까지 온거리에 x2 이므로 어떤 거리라도 1만큼은 무조건 점프를 해줘야 한다.
# 에너지 사용의 최소값을 구해야 하기 때문에 n의 총 길이를 2로 나눴을 때 나머지가 1과 같다면
# 에너지 사용 1을 추가하는 조건식을 넣어주고, n을 //=, 반복할 n을 2로 나누어 주면서 최소로 반복하고 답을 구할 수 있도록
# 코드를 작성했다.

def solution(n):
    answer = 0
    while n:
        if n % 2 == 1:
            answer += 1
        n //= 2
    return answer


def test_solution():
    assert solution(5) == 2
    assert solution(6) == 2
    assert solution(5000) == 5

