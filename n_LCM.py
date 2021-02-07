# n개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

# 배열안에 이미 약수인 값들을 0으로 지워주고 arr배열에 남아있는 값 중 최대값을 변수로 지정한다.
# arr의 모든 수로 나눠지는 수가 나올때까지 tmp의 값이 1씩 증가하고
# 모든 수로 나눠 떨어지는 경우 return 해서 해결한다.

def solution(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] != 0 and arr[i] % arr[j] == 0:
                arr[j] = 0
    tmp = max(arr)
    while True:
        for a in arr:
            if a != 0 and tmp % a != 0:
                break
            if a == arr[-1]:
                return tmp
        tmp += 1

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))