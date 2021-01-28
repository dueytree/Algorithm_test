# 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919

# 변수 x에 index함수로 문자열의 위치값을 넣어주고
# answer 값에 출력할 문장을 넣고, x의 값이 int값이기 때문에 str(x)로 넣어준다.

def solution(seoul):
    x = seoul.index('Kim')
    answer = '김서방은 '+str(x)+'에 있다'
    return answer

# def solution(seoul):
#     return f"김서방은 {seoul.index('Kim')}에 있다"

print(solution(["Jane", "Kim"]))