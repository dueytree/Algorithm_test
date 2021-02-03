# 정수 내림차순으로 정리하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

# 앞서 문자열 내림차순으로 정리하기에서 배웠던 join, reverse 내장함수를 사용해
# 정수를 내림차순으로 정리해 주었다. 특별히 다른점은 주어진 s의 값이 int이므로 str로 덮어주어
# 내림차순으로 정렬해줘야 가능하고 마지막에 int로 감싸줘야한다.

def solution(s):
    return int(''.join(sorted(str(s), reverse=True)))

print(solution(118372))