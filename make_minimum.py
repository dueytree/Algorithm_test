# 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941

# 배열 A, B 에서 각 인덱스의 곱을 최소로 계산해 더한 값을 출력해야 한다. 같은 인덱스의 수끼리는 곱할 수 없고,
# 각 수가 모두 곱해지므로 배열의 길이는 서로 같다.
# 첫번째 답에서 답을 출력할 answer변수를 만들고, A의 배열은 정렬, B의 배열은 reverse 뒤집어준 다음,
# A, B의 길이가 같기 때문에 len(A)만큼 범위를 정해주고 answer에 곱을 모두 더해주는 식을 써주었다.
# 여기서 첫번째 답은 단순히 B의 배열을 reverse, 즉 뒤집기만 시켜주고 정렬은 해주지 않았기 때문에 가운데 인덱스 값이 바뀌지 않아
# 정확도 검사에서 오답으로 처리되는 것으로 봤다. 이럴 때 B.sort(reverse=True) 처리를 해줌으로 뒤집기와 동시에 정렬을 시켜준다.


# 오답
# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.reverse()
#     for i in range(len(A)):
#         answer += A[i] * B[i]
#     return answer
#
# print(solution([1, 4, 2], [5, 4, 4]))


def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

def test_solution():
    assert solution([1, 4, 2], [5, 4, 4])
    assert solution([1,2], [3,4])