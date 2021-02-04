# 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

# 제공되는 map 입력을 사용하여 a, b 입력값을 받고
# for문으로 가로, 세로의 길이를 동시에 돌려주는 방법으로 진행한다. 반복문이 돌때마다 별을 출력하지만 마지막엔
# 공백을 채워주고 반복문 탈출 후 빈 프린트를 넣어서 줄바꿈을 표현해 결과값에 맞춰준다.

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()