# 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994

# 문제 설명에서 U, D, R, L 설명으로 캐릭터가 좌표평면 위치에 나타나 있고, 입력받은 값을 위치에 적용시켜
# 처음 걸어본 길의 길이를 구하는 문제이다.
# 걸어간 길이를 담아 마지막에 길이를 출력해줄 answer값, 현재 위치를 기준으로 한 start[0, 0] 값을 지정하고
# 입력값 dirs을 element 반복하여 위, 아래, 왼쪽, 오른쪽을 조건문으로 잡아 준 뒤
# end 값을 지정하고, 좌표평면의 경계를 조건으로 잡고, 그 안에 조건문으로 answer 값 안에 이미 한번 지나간 길의
# 값을 비교해준다. 없을 시 answer 값에 시작과 끝 값을 넣어주고, 마지막으로 end값을 start로 넣어주고
# 반복문을 끝까지 돌아준다. 반복문이 끝나고 마지막에 answer의 길이를 리턴한다.

def solution(dirs):
    answer = []
    start = [0, 0]

    for element in dirs:
        if element == 'U':
            element = [0, 1]
        elif element == 'D':
            element = [0, -1]
        elif element == 'R':
            element = [1, 0]
        elif element == 'L':
            element = [-1, 0]
        end = [start[0] + element[0], start[1] + element[1]]
        if -5 <= end[0] <= 5 and -5 <= end[1] <= 5:
            if [start, end] not in answer and [end, start] not in answer:
                answer.append([start, end])
            start = end
    return len(answer)

def test_solution():
    assert solution("ULURRDLLU") == 7
    assert solution("LULLLLLLU") == 7