# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

# for문으로 reserve만큼 반복하는데, if문으로 잃어버린 학생들을 reserve에서 -1, +1 한 값에서 지워주는 조건을 걸어주고
# (체육복 남는 친구 - 잃어버린 친구), 마지막에 빌린친구들을 제외하고 체육시간에 참여하지 못한 학생들을 구해주는 값을 구해준다.
# 전체학생 수  - 잃어버린 학생의 수
# 여벌을 챙긴 학생이 체육복을 도난 당했을 수도 있다. 그 학생은 하나만 도난당했다고 가정하고, 친구에게 빌려줄 수 없다.
# 문자열은 immutable, set 내장함수로 감싸서 처음부터 도난당한 학생과 여벌옷을 챙긴 학생의 중복을 제외하고 시작한다.

def solution(n, lost, reserve):
    some_reserve = set(reserve) - set(lost)
    some_lost = set(lost) - set(reserve)
    for element in some_reserve:
        if element - 1 in some_lost:
            some_lost.remove(element - 1)
        elif element + 1 in some_lost:
            some_lost.remove(element + 1)
    return n - len(some_lost)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))