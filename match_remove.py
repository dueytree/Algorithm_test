# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

# 첫번째 해답은 단순히 반복문 while와 조건문 if로 문제 해결을 나열했는데, 확실히 시간복잡도 부분에서 너무 많은
# 시간을 잡아먹었다. 첫 if문은 짝지어 제거하기 첫 조건으로 문자열 길이의 홀-짝 여부를 판별하는 조건문이고
# 다음은 while문으로 모든 값을 돌게끔 지정한 뒤, 짝지어 제거하는 계산을 나열했다.

# def solution(s):
#     if len(s) % 2 == 1:
#         return 0
#     i = 0
#     while True:
#         if len(s) == 0:
#             return 1
#         if i > len(s) - 2:
#             return 0
#         if s[i] == s[i + 1]:
#             if i == 0:
#                 s = s[i + 2:]
#             else:
#                 s = s[:i] + s[i + 2:]
#                 i = 0
#         else:
#             i += 1


# 시간복잡도 관련해 stack을 이용한 해답이다.
# 빈 리스트 answer를 잡아주고 문자열 s의 i 반복문으로 answer의 값이 없을 때 문자열 s의 값을 하나 넣어주고
# i의 값이 LIFO, 마지막에 들어온값이 i와 같을 때 짝지어 삭제해주고, 같지 않을 시에 i를 그대로 answer에 넣어주어
# 반복문을 끝까지 실행한다. 마지막 if문은 문제 조건에 맞춰 answer의 값이 없으면 1, 그렇지 않으면 0을 return해주는 방식으로 진행하였다.

def solution(s):
    answer = []
    if len(s) % 2 == 1:
        return 0
    for i in s:
        if len(answer) == 0:
            answer.append(i)
        elif i == answer[-1]:
            answer.pop()
        else:
            answer.append(i)
    if len(answer) == 0:
        return 1
    else:
        return 0


def test_solution():
    assert solution("baabaa") == 1
    assert solution("cdcd") == 0