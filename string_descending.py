# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

# 간단히 sorted 함수로 문자열을 나열해 줬는데 각 알파벳 하나씩 문자열로 나타나서 join 함수로
# 문자열을 합쳐주고, reverse함수로 문자열을 뒤집어서 나열해주었다.

def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))