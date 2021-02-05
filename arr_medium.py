# 평균 구하기
# https://programmers.co.kr/learn/courses/30/lessons/12944

# 입력받은 배열을 모두 더한 뒤 그 값을 배열의 범위 만큼 나눠서
# 배열의 평균을 구해준다

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return answer / len(arr)

print(solution([1, 2, 3, 4]))
print(solution([5, 5]))
