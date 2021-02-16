# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

# 숫자가 크면 클수록 중요도가 높기때문에 리스트에 가장 큰 수를 찾는다. 그리고 for문으로 priorities범위 설정하고
# 만약 가장 큰수와 리스트[i] 값이 같을때 answer값에 +1을 해주고 그 리스트 인덱스 i의 값을 출력완료로 0을 넣어준다.
# 그리고 다시 max_p의 값을 설정해주고, 그 if문 안에서 if문으로 i가 location 값과 같을때 answer 값을 리턴해준다.
# for문 상위에 while True문을 사용해 줘야 리스트안에 모든 출력들을 완료하고 0을 출력할때까지 진행한다.

def solution(priorities, location):
    answer = 0
    max_p = max(priorities)
    while True:
        for i in range(len(priorities)):
            if max_p == priorities[i]:
                answer += 1
                priorities[i] = 0
                max_p = max(priorities)
                if i == location:
                    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))