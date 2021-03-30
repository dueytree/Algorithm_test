# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

# 4열씩 주어지고 땅은 2차원 배열로 주어진다고 한다. 그리고 첫번째 열에서 첫번째 칸을 밟았다면, 두번째 열에서
# 첫번째 칸을 밟을 수 없다. 같은 칸의 땅을 연속해서 밟을 수 없다. 그래서 밟은 땅을 뺀 땅의 최대값을 구해줘야한다.
# 첫번째 줄과 두번째 줄을 바탕으로 반복문을 설정 해주고, 연속적으로 같은 칸을 밟을 수 없게 끔 설정해준다.
# 그리고 반복문 마지막에 식에서 윗줄의 j열 빼고 만든 리스트에서 최대값을 뽑아 더해주도록 한다.
# max값 내부 식에서 앞쪽 식에서는 j열 앞까지, 뒷쪽 식에서는 j열 + 1부터 끝까지 값을 서로 더해 max값을 뽑아
# 넣어주고 return한다.


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[len(land) - 1])

def test_solution():
    assert solution([[1,2,3,5], [5,6,7,8], [4,3,2,1]]) == 16