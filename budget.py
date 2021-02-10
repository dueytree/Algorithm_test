# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

# 최대한 많은 부서에 지원을 해주기 때문에 가장 적은 신청금액부터 처리한다. d를 정렬시켜주고
# d의 길이범위 만큼 돌고 if문으로 d의 값이 반복될때마다 예산을 차감해나가고, answer 값을 1씩 올려주면서 진행한다.

def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
