# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

# 입출력 예시 단계 중 3진법을 건너 뛰고 10진법으로 표기했는데, 3진법 뒤집는 것을 while문으로 진행한다. 3진법 계산용 변수를 만들어주고
# for문으로 3진법으로 저장한 변수 tmp를 뒤집은 값을 돌려서 답에 반복되는 int값, 계산용 변수를 곱해준 것을 넣어주고
# 마지막에 계산용 변수에 3을 반복해 곱해주는 식을 넣어준다.

def solution(n) :
    answer = 0
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = int(n / 3)
    count = 1
    for i in reversed(tmp):
        answer += int(i) * count
        count *= 3

    return answer

print(solution(45))
print(solution(125))