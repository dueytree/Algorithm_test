# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

# 괄호가 올바르게 지정되려면 쌍을 이뤄야하고, 아무리 겹쳐서 쌓인다고 해도 서로 짝이 맞으면 괄호를 사용할 수 있다.
# 단순히 괄호를 한개씩 비교해서는 복잡하고, stack을 사용해 시작괄호 ( 를 넣고, 끝 괄호 ) 가 보이면 시작괄호를 하나씩 삭제하며
# 올바르게 괄호가 사용되었는지 확인하면 단순할 것이라고 생각했다.
# 빈 리스트를 하나 만들고, s 반복문을 돌려 element에 ( 시작괄호가 있으면 리스트에 넣어주고, else 아래에 if문을 하나 더 넣어서
# 리스트 길이가 0일때,(시작괄호를 지워줄 끝 괄호가 없을 때) False를 리턴하고, 아닐때 시작괄호를 지워줄 pop()을 이용한다.
# 마지막으로 return에 0과 정답 리스트의 길이를 불린형으로 넣어 T,F 로 확인할 수 있게끔 지정해 준다.

def solution(s):
    answer = []
    for element in s:
        if element == "(":
            answer.append(element)
        else:
            if len(answer) == 0:
                return False
            else:
                answer.pop()
    return len(answer) == 0

def test_solution():
    assert solution("()()") == True
    assert solution("(())()") == True
    assert solution(")()(") == False
    assert solution("(()(") == False