# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 제한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

# 짝수일때 가운데 2개, 홀수일때 가운데 1개를 출력해야한다. if문을 사용해서
# len(s) 길이가 홀수일때 2로 나눠 남은 값으로 가운데 값을 구하고, 짝수일때 가운데 값 -1 을 넣어
# 두개의 값을 구하는 방법


def solution(s):
    a = len(s)
    if a % 2 == 1:
        return s[a // 2]
    else:
        return s[a // 2 - 1 : a // 2 + 1]


print(solution("abcde"))
print(solution("qwer"))
print(solution("qwerqwer"))