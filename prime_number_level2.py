# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

# 순열과 조합의 문제에서 itertools에 permutations를 import 해서 사용하면 원소의 갯수를 지정해 수열을 만들 수 있다.
# numbers의 전체 순열을 넣어줄 리스트 num_list를 만들어 주고, for문으로 1부터 numbers의 길이에 +1 해주고
# 임시변수 tmp에 numbers에 i의 갯수만큼 permutations을 사용해 수열을 만들어 넣어준다.
# 그 tmp 만큼 j반복문을 돌려 num_list에 순열을 문자열로 합치고 정수형으로 넣어준다.
# 그리고 num_list를 리스트로 변형시켜준 뒤 answer 변수에 num_list의 길이를 넣어주고
# for문을 num_list만큼 돌려 소수를 판별해 주는 식으로 넣어주고 answer를 return해준다.

from itertools import permutations

def solution(numbers):
    num_list = []
    for i in range(1, len(numbers) + 1):
        tmp = permutations(numbers, i)
        for j in tmp:
            num_list.append(int(''.join(j)))
    num_list = list(set(num_list))
    answer = len(num_list)
    for i in num_list:
        if i < 2:
            answer -= 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                answer -= 1
                break
    return answer


def test_solution():
    assert solution("17") == 3
    assert solution("011") == 2