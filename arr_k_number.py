# k번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748

# i번째 숫자부터 j번째 숫자까지 array배열에서 자른 후, 정렬해준다음 k번째 숫자를 얻어야 한다.
# commands 배열에 i,j,k,값이 차례대로 제공되는데 for 문으로 i,j,k 값을 commands안에서 돌려준 후
# 빈 배열 answer에 정렬함수 sorted(array[i부터 j까지(0부터 시작이니 -1)[k번째 수, 0부터 시작이니 -1]) 를 사용해서
# append로 answer값에 넣어준뒤 for문에서 빠져나와 return한다.

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1 :j])[k - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))