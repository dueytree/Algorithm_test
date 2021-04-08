# 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844

# 이 문제는 최단거리를 구하는 문제이므로, 전에 배웠던 BFS를 생각해 풀이했다.
# 주어진 그림으로 map을 구상해 직접 그려서 경로를 1로 표현, 아닌 곳은 0으로 표현해 직접 표를 그려보면
# 이해하기가 쉽다.

from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[x][y] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1

def test_solution():
    assert solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) == 11
    assert solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) == -1