# 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

# for문 안에 if문을 넣어 각 인덱스 마다 비교해 가장 작은 수를 찾았을 때 삭제해주는 방법으로 진행.

def solution(arr):
    small_num = min(arr)
    if len(arr) > 1:
        arr.remove(small_num)
        answer = arr
    else:
        answer = [-1]
    return answer

print(solution([4,3,2,1]))
print(solution([10]))