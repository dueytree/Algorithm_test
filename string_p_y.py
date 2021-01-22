# 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916
# p와 y값을 비교해 갯수를 저장할 변수 하나씩 만들어 주고, 대문자와 소문자를 if문으로 동시에 비교해
# 포함될시 각 변수에 1을 추가해 줌으로 갯수를 확인해 나간다. 이후 answer값에 if문으로 p와 y값을
# 비교해 True False를 나타내게 진행했다.

def solution(s):
    answer = True
    P = 0
    Y = 0

    for i in s:
        if i == 'p' or i == 'P':
            P += 1
        elif i == 'y' or i == 'Y':
            Y += 1

    answer = True if P == Y else False
    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))