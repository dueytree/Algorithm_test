# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

# 어떠한 수가 입력되면, 그 수로 각 자리의 합을 구한 후에 그 수를 나누었을 때
# 나눠 떨어지면 True, 떨어지지 않으면 False를 출력한다.

def solution(x):
    str_x = str(x)
    tmp = 0
    for i in str_x:
        tmp += int(i)
    if x % tmp == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
