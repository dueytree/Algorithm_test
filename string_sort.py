# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

# strings의 길이 범위만큼 for문을 돌려 n번째 값을 strings 단어 앞에 붙인다음
# sort 정렬 해주고 다시 strings 값의 범위만큼 돌려 n번째 값을 붙인 단어를 초기화 시켜준다.

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for j in range(len(strings)):
        answer.append(strings[j][1:])

    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
