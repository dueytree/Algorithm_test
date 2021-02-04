# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

# arr1 범위만큼 반복문을 작성하고, 빈 리스트 변수를 하나 설정한 다음, arr1 for문 안에 arr1 인덱싱 반복하는
# 반복문을 만들어주고 tmp 빈 리스트에 arr1[i][j] + arr2[i][j] 값을 넣어준다. 마지막에 answer 리스트에 담아주고 리턴해준다.

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))