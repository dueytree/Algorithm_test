# 이진변환 반복하
# https://programmers.co.kr/learn/courses/30/lessons/70129

# 입력된 값에서 모든 0을 제거하고, 제거한 변환한 횟수와 제거된 모든 0의 갯수를 리턴해야한다.
# 횟수를 담아줄 cnt, 0이 삭제된 갯수를 담아줄 zero 변수를 지정하고, while 문을 사용해 1이 아닌 문자열을
# 제외한 모든 값을 돌게 한다. cnt는 횟수마다 1씩 증가, strg 변수를 지정하고 1을 담아준다.
# zero 변수에 입력값 s의 길이 - 1을 담아둔 strg를 뺀 값을 더해주고
# s에 이진변환을 해 담아준다. 이 과정을 반복한 후 cnt와 zero를 리스트에 담아 return한다.

def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        cnt += 1
        strg = s.count('1')
        zero += len(s) - strg
        s = bin(strg)[2:]
    return [cnt, zero]

def test_solution():
    assert solution("110010101001") == [3, 8]
    assert solution("01110") == [3, 3]
    assert solution("1111111") == [4, 1]