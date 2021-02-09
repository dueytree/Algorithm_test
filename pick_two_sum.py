# 두개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

# 배열에 포함된 모든 수가 서로 더해져야하기 때문에 for문을 두번 사용해 값을 구한다.
# 첫번째 for문은 기준이 되는 수로 0부터 배열의 길이범위 만큼 돌아주고, 두번째 for문은 더해지는 수로
# 배열의 i 보다 + 1을 설정해준다. 이렇게 더해져 나온 값을 answer 배열에 append 해주고
# 결과 값에 공통된 값이 없어야하고 정렬되어야 함으로 sorted, set함수를 사용해준다.

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i + 1:]:
            answer.append(numbers[i] + j)
    return sorted(set(answer))

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))