# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

# 첫번째 풀이는 brown과 yellow의 합을 carpet_count 임시변수에 넣어주고 for 문으로 가로의 길이를 반복하여
# i로 카펫의 갯수를 나눴을 때 나머지가 없을 시 세로의 길이를 얻고 안쪽 카펫의 갯수가 yellow와 같을 시
# 가로 세로의 값을 return한다.

# 두번째 풀이는 첫번째 풀이 전에 brown과 yellow의 길이를 방정식 문제로 접목시켜 가로를 x로 세로를 y로 잡아
# x를 구하는 식을 넣어 구하고, 전체 개수에 x를 나눠 y의 값을 구한 다음 가로 세로 길이 중 큰 값이 가로의 길이 이므로
# max 와 min 함수를 사용해 return 했다.
# 방정식 계산이 생각이 잘 나지 않아 첫번째 풀이로 풀고 두번째 풀이로 풀었는데
# 확실히 두번째 풀이가 시간복잡도가 굉장히 낮았다.



# 첫번째 풀이
def solution(brown, yellow):
    cp_count = brown + yellow
    for i in range(cp_count, 2, -1):
        if cp_count % i == 0:
            length = cp_count // i
            if yellow == (i - 2) * (length - 2):
                return [i, length]


# 두번째 풀이
# def solution(brown, red):
#     x = (brown + 4 + ((brown + 4) ** 2 - 16 * (brown + red)) ** 0.5) / 4
#     y = (brown + red) // x
#     return [max(x, y), min(x, y)]


def test_solution():
    assert solution(10, 2) == [4, 3]
    assert solution(8, 1) == [3, 3]
    assert solution(24, 24) == [8, 6]