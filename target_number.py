# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

# 이 문제의 풀이 방향성은 깊이 너비 탐색, DFS-BFS 문제다. 너비 우선탐색을 사용해(BFS)를 생각해 풀었다.
# DFS 방식으로 반복적으로 풀이되는 방법이다. answer 리스트는 0부터 시작해서 각 계산을 하는 기준으로 반복된다.
# for문을 numbers 길이만큼 반복되며 더하고 뺀 값을 저장할 storage 리스트를 지정한 후 j 반복문으로 j - i, j + i 계산을
# 반복적으로 돌린 후 반복문이 끝나고 answer 리스트에 계산한 storage 리스트를 넣어준 뒤
# answer 리스트에 target의 수가 몇개 있는지 return해준다.

def solution(numbers, target):
    answer = [0]
    for i in range(len(numbers)):
        strg = []
        for j in range(len(answer)):
            strg.append(answer[j] - numbers[i])
            strg.append(answer[j] + numbers[i])
        answer = strg
    return answer.count(target)


def test_solution():
    assert solution([1, 1, 1, 1, 1], 3) == 5