# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

# 두 배열을 정렬한뒤에 하나씩 element가 일치하는지 확인하는 방식으로
# 간단히 for문으로 참여선수들을 반복하고 그 안에 if문을 넣어서 참여선수들 중 완주하지 않은 선수가 있을때 return 해주는 방법
# 마지막 return문이 있어야 완주하지 못한 선수가 출력된다.

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["marina", "josipa", "nikola", "filipa"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "ana"]))
