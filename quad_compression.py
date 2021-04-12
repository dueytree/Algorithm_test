# 쿼드압축 후 개수 세
# https://programmers.co.kr/learn/courses/30/lessons/68936

# 이 문제를 보고 재귀함수를 생각했다.
# 분할 좌표를 구할 때 기준 좌표와 길이가 있으면 구할 수 있으므로 재귀함수 인자는 (행 좌표, 열 좌표, 분할된 길이, 기존 배열)으로 하면 된다.
# answer = check(0, 0, len(arr), arr)로 시작하면,
# 왼쪽 윗부분은 (시작 좌표, 시작 좌표)
# 오른쪽 윗부분은 (시작 좌표, 시작 좌표 + n // 2)
# 왼쪽 아랫부분은 (시작 좌표 + n // 2, 시작 좌표)
# 오른쪽 아랫부분은 (시작 좌표 + n // 2, 시작 좌표 + n // 2)
# 이렇게 분할된 좌표를 알 수 있다.
#
# 사각형 길이가 1이면 1, 0으로 return 한다.
# 만약 길이가 1이 아니면 왼쪽 윗부분부터 오른쪽 아랫부분까지 사각형 길이가 1이 될 때까지 분할한다.
# 재귀 함수가 return이 시작된다면 사각형 길이가 1인 부분부터 구역이 합쳐지면서 2가지를 고려하면 된다.
#
# 합쳐진 구역이 모두 같은 값인지
# 합쳐진 구역에 다른 값이 있는지
# 구역이 모두 같은 값이면 구역 중 한가지 값으로 return 해줘서 다음에 합쳐지는 구역으로 값을 넘겨주고,
# 구역에 다른 값이 있으면 구역에서 1과 0의 개수로 return 해줘서 다음에 합쳐지는 구역에 값을 넘겨주면 된다.

def check(x, y, n, arr):
    if n == 1:
        if arr[x][y] == 1:
            return [0, 1]
        else:
            return [1, 0]

    left_up = check(x, y, n // 2, arr)
    right_up = check(x, y + n // 2, n // 2, arr)
    left_down = check(x + n // 2, y, n // 2, arr)
    right_down = check(x + n // 2, y + n // 2, n // 2, arr)

    if left_up == right_up == left_down == right_down == [0, 1] or left_up == right_up == left_down == right_down == [1, 0]:
        return left_up
    else:
        return list(map(sum, zip(left_up, right_up, left_down, right_down)))

def solution(arr):
    answer = check(0, 0, len(arr), arr)
    return answer

def test_solution():
    assert solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4, 9]
    assert solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]) == [10, 15]