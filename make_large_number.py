# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

# 숫자 number를 숫자 갯수만큼 돌아주는 for문을 사용해 for 문 안에서 while문으로 answer 값을 받고 제거할 수의 갯수를 0보다 큰,
# answer[-1]의 값을 number[i] 보다 작은 조건을 성립해 주어진 1,9,2,4 숫자를 반복시켜 가장 큰 수를 비교해 맨앞으로 설정,
# 그 다음자리 수를 다시 비교해 큰 수를 설정해 줌으로 k 갯수만큼 제외하고 가장 큰 수를 구할 수 있게 적용한다. 구하는 과정 속
# pop()를 사용해 비교시 필요없는 수를 제외시켜주고, 가장 큰 수가 조건에서 빠져나왔을때 k의 값을 하나씩 줄여준 후 while반복문에서
# 빠져나올때 answer 값에 append 해주는 방식으로 진행한다. 마지막 return에서는 join으로 문자열 덮어주고, number의 길이를 k로 제외한
# answer의 인덱스 값을 지정해준다.

def solution(number, k):
    answer = []
    for i in range(len(number)):
        while answer and k > 0 and answer[-1] < number[i]:
            answer.pop()
            k -= 1
        answer.append(number[i])
    return ''.join(answer[:len(number)-k])


def test_solution():
    assert solution("1924", 2) == "94"
    assert solution("1231234", 3) == "3234"
    assert solution("4177252841", 4) == "775841"
