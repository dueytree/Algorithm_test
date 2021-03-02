# 가장 큰 정사각형
# https://programmers.co.kr/learn/courses/30/lessons/12905

# 우선 같은 행과 열에 1이 포함되어있는지 확인해야한다. 정사각형이기 때문에 예를 들어
# 2열부터 4열까지, 2행부터 4행까지 숫자 1 값이 있어야 3 * 3 정사각형이 만들어진다.
# 반복문을 두개를 적용해 board 길이범위까지 정하고, 두번째 반복문 j에 board의 가장 앞 인덱스를 넣어준 뒤
# if문을 통해 1의 값 유무를 판별하는 조건을 넣어준다.(이때, 각 i와 j값도 0보다 크다는 것을 지정해 주어야한다.)
# 2 * 2 행과 열값이 주어져야 사각형이 만들어지기 때문에 값을 지정해주는 식을 넣어준다.
# return 값으로는 변의 길이에 제곱을 해주어 전체 사각형 값을 나타낸다.

import pytest

def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i > 0 and j > 0 and board[i][j] != 0:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
            answer = max(answer, board[i][j])
    return answer ** 2

def test_solution():
    assert solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9
    assert solution([[0,0,1,1],[1,1,1,1]]) == 4