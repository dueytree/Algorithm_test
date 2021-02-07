# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

# 문자열을 쪼개주기 위해 split을 사용하고, 그 쪼갠 문자열을 담아주기 위해 변수를 사용한다.
# 그리고 홀수와 짝수번째 알파벳을 구별하는식으로 for문과 if문으로 upper, lower 함수를 이용해 해결한다.

def solution(s):
    s_list = s.split(' ')
    answer = []
    for element in s_list:
        s = ''
        for i in range(0, len(element)):
            if i % 2 == 0:
                s += element[i].upper()
            else:
                s += element[i].lower()
        answer.append(s)
    return ' '.join(answer)

print(solution('try hello world'))