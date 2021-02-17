# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 배포준비가 끝난 수를 담는 count변수와 하루씩 지나는 시간을 정해놓은 days변수를 지정하고
# while 문을 사용해 progresses의 길이가 0보다 클때를 지정해놓고
# progresses의 첫번째 인덱스가 100보다 크거나 같을때 개발이 완료된 것으로 개발수치, 날짜, 개발속도를 계산한 값을 조건으로 넣어주고
# 조건에 일치할때 progresses와 speed의 가장 앞의 값을 pop를 사용해 제거한 후 배포 갯수를 1 늘려준다.
# 조건에 일치하지 않을때 배포가능 갯수가 0보다 클때를 설정해 놓고 0보다 클시에 count의 값을 answer값에 넣어준다. 그리고 답을 리턴한다.

def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))