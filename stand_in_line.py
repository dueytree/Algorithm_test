# 줄 서는 방법
# https://programmers.co.kr/learn/courses/30/lessons/12936

# 단순하게 사람 수만큼의 리스트를 1부터 n까지 넣어 만들고, 그에 따른 모든 경우의
# 사람 수 n을 받아 1부터 n까지의 값을 넣어준 n_list를 permutations함수로 순열을 만들어 진행했으나
# 시간초과 발생, n이 아닌 바로 답을 구할 수 있는 방법을 찾아야 한다.
# 이 문제가 가장 앞자리 수에 따라 경우가 달라지는 것을 쉽게 알 수 있다. 규칙으로 첫번째 올 수 있는 경우의 수는
# (n - 1)! 과 같다. 이를 통해 k의 값을 n-1로 나눠 첫번째 자리에 어떤 숫자가 오는지 알 수 있다.
# while문을 사용했고, n의 값이 0이 아닐때를 조건으로 factorial 함수와 append, pop 함수를 사용해 n_list의 값들을
# answer 리스트에 넣어준 뒤 return했다.

from math import factorial
def solution(n, k):
    answer = []
    n_list = list(range(1, n + 1))
    while n != 0:
        case = factorial(n - 1)
        answer.append(n_list.pop((k - 1) // case))
        n, k = n - 1, k % case
    return answer


def test_solution():
    assert solution(3, 5) == [3, 1, 2]

