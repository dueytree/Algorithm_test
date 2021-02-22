# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

# number 배열의 값을 이용해 가장 큰 수를 만들어야한다. 그리고 마지막에 문자열로 변환하여 return해야한다.
# map 내장함수와 lanbda함수를 사용해 풀이한다.
# 일단 map 내장함수로 number값을 문자열로 맵핑하고, key와 lambda값을 number 원소값이 1000 미만이기 때문에 x: x * 3으로 지정,
# 그 값을 list로 덮어씌워 변환해준다음, sorted로 정렬한 뒤 join으로 문자열을 합쳐준다. 이후에 바로 출력하게되면
# member의 원소값이 모두 0일때 값이 000 으로 나오기때문에 문자열 변환 전 정수형으로 변환해준 다음 문자열로 변환해준다.

def solution(number):
    return str(int("".join(sorted(list(map(str, number)), key=lambda x: x * 3, reverse=True))))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))