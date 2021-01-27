# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

# if문으로 길이 조건, 숫자로만 구성되어 있는지 확인해주고 조건에 따라 불린 형식으로
# 리턴해주는 방식이다.

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False


print(solution("a234"))
print(solution("1234"))