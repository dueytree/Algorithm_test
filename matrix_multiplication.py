# 행렬의 곱
# https://programmers.co.kr/learn/courses/30/lessons/12949

# arr1 행의 값과 arr2 열의 값을 곱해야 한다. for문을 3개 사용하고, arr1 행을 도는 for문에
# 계산된 모든 값을 담을 빈 리스트를 만들어주고 열의 첫번째값의 길이를 도는 반복문 안에 계산된 값을 저장할 변수를 지정한다.
# k 반복문에서 각 행렬의 곱을 빈 저장소에 넣어주고, 계산이 끝나면 반복문을 나와 total 리스트에 append 해준다.
# 다시 strg는 0으로 초기화 되고, 이 과정을 반복한 후 전체 계산이 종료되면 answer 리스트에 append 해줘서
# [[0, 0], [0, 0]] 리스트 안에 리스트로 출력하도록 설정한다.

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        total = []
        for j in range(len(arr2[0])):
            strg = 0
            for k in range(len(arr2)):
                strg += arr1[i][k] * arr2[k][j]
            total.append(strg)
        answer.append(total)
    return answer


def test_solution():
    assert solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [[15, 15], [15, 15], [15, 15]]
    assert solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]