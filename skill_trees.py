# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

# for문을 사용해 스킬트리에서 반복되는 element값을 설정해 주고, 빈 리스트를 만들어 준다음, 스킬의 순서와
# 스킬트리에서 skill의 값만 남겨놓은 storage를 비교할 불린형 current를 만들어준다.
# element 범위만큼의 반복문을 만들어 주고 skill 리스트 안에 element 값을 storage에 담아준다.
# 다음엔 storage 범위의 반복문으로 if문을 사용해주고 storage와 skill 인덱스를 비교해주는 조건을 걸어주고
# 같이 않을때 current = false로 설정하고 break로 반복문을 멈춰준다. (스킬트리는 순서가 정해져 있기 때문)
# 만약 break로 멈추지 않고 스킬트리가 조건에 맞을때 current = True값으로 설정해주고 answer의 값을
# 1씩 올려준다.

def solution(skill, skill_trees):
    answer = 0
    for element in skill_trees:
        storage = []
        current = True

        for i in range(len(element)):
            if element[i] in skill:
                storage.append(element[i])
        for j in range(len(storage)):
            if storage[j] != skill[j]:
                current = False
                break
        if current == True:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# def solution(skill, skill_trees):
#     answer = len(skill_trees)
#     for skill_tree in skill_trees:
#         skill_tree_list = [skill_tree_element for skill_tree_element in skill_tree if skill_tree_element in skill]
#         for j in range(len(skill_tree_list)):
#             if skill_tree_list[j] != skill[j]:
#                 answer -= 1
#                 break
#     return answer