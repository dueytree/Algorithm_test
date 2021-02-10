# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

# 각 학생의 패턴과 맞춘 문제를 담은 변수를 만들어 주고, 정답의 길이만큼 for문을 돌려준 뒤, 각 학생의 n번째 문제의 정답을
# 구해주는 조건을 넣어서 정답일시 정답 count 변수에 넣어준다. 그리고 각 학생의 정답을 맞춘 갯수를 tmp 임시 변수에 넣어주고
# for문을 score와 element로 반복하고 enumerate로 tmp 돌려준 뒤 정답과 tmp 가장 큰값이 같을 때 빈 정답 변수 answer에
# element + 1 한 값을 넣어준다. (0부터 시작이므로)

def solution(answers):
    answer = []
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s_1_count = 0
    s_2_count = 0
    s_3_count = 0

    for i in range(len(answers)):
        if answers[i] == student_1[i % 5]:
            s_1_count += 1
        if answers[i] == student_2[i % 8]:
            s_2_count += 1
        if answers[i] == student_3[i % 10]:
            s_3_count += 1

    tmp = [s_1_count, s_2_count, s_3_count]
    for element, score in enumerate(tmp):
        if score == max(tmp):
            answer.append(element + 1)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))