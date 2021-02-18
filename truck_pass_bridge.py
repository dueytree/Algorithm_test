# 다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583

# 다리길이에 트럭이 1초에 1씩 빠져나오기때문에 무게만 허용된다면 트럭이 다리에 2대씩 있을수도 있다.
# 시간을 구해야하기 때문에 answer값을 0으로 변수를 잡아주고
# 트럭이 지나가는 과정의 값을 진행시키기 위해 pass_truck 변수를 만들어준다.
# 항목 전체 다 끝날때까지 돌아야하기때문에 while문을 사용해서 += 시간을 1씩 넣어주고
# pass_truck 가장 마지막 인덱스에 들어온 0을 제거해주는 식을 넣어준 뒤
# if문을 사용해 허용 무게보다 같거나 작은 (pass_truck의 합) + (가장 앞의 트럭 무게) 값을 넣어줘서
# 조건에 허용할시 통과예정인 pass_truck에 가장 앞 인덱스의 값을 넣어줘서 다리를 지나가게끔 해준다.
# 뒤에 pass_truck에 0을 넣어줌으로서 뒷트럭이 진행될수 있도록 해준다.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    pass_truck = [0] * bridge_length
    while pass_truck:
        answer += 1
        pass_truck.pop(0)
        if truck_weights:
            if (sum(pass_truck) + truck_weights[0]) <= weight:
                pass_truck.append(truck_weights.pop(0))
            else:
                pass_truck.append(0)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))