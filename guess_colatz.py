# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

# num이 1일때 바로 끝나는 if 문을 넣어주고, 몇번만에 1이 되는지를 담아주는 tmp 변수를 설정한 뒤
# for 문을 한계 범위인 500까지 잡은 뒤 if 문에 홀수와 짝수의 계산 식을 넣어준뒤, tmp의 값을 1씩 올려준다.
# 만약 수가 1이 되었을때 return tmp 해주고, 다 돌았는데도 1로 빠져나오지 못했을때를 생각해 for문을 빠져나온 뒤
# return -1을 해준다.

def solution(num):
    if num == 1:
        return 0
    tmp = 0
    for i in range(500):
        if num % 2 != 0:
            num *= 3
            num += 1
        else:
            num /= 2
        tmp += 1

        if num == 1:
            return tmp

    return -1


print(solution(6))
print(solution(16))
print(solution(626331))