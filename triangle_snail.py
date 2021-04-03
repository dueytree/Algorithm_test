# 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

# 피라미드 모양의 삼각형에서 주어진 n값으로 반시계 방향으로 돌며 수를 채우는데, 첫 행부터 마지막행까지 모든 순서를 나열한 리스트를
# return해야 한다. 달팽이 값을 저장할 n의 길이만큼의 0 값 리스트를 n개 만들어주고, 인덱스에 접근해 수를 넣어주어야 하기 때문에
# a, b의 변수를 지정한다. 그리고 저장할 수 num을 지정한다. for문을 이중으로 한쪽 변을 지날때마다 n개에서 1개로 저장할 숫자가
# 작아지니까 0~n, i~n까지의 for문을 지정해 준다. 그리고 if문으로 위로갈지, 아래로 갈지, 오른쪽으로 돌지를 조건문을 만들어주고,
# 맞는 인덱스에 숫자(num)를 1씩 증가하여 return에 append, 넣어준다.

def solution(n):
    base_list = [[0] * n for _ in range(n)]
    answer = []
    a, b = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                a += 1
            elif i % 3 == 1:
                b += 1
            elif i % 3 == 2:
                a -= 1
                b -= 1
            base_list[a][b] = num
            num += 1
    for i in base_list:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer


def test_solution():
    assert solution(4) == [1,2,9,3,10,8,4,5,6,7]
    assert solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
    assert solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]