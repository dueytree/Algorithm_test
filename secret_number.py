# 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

# 뒷 4자리를 *로 표시할때는 쉽지만 뒷 4자리를 제외하고 *로 처리할때는
# len(num) - 4 를 통해 뒷 4자리를 제외한 범위를 '*'로 곱해줘 *처리하고 마지막에 다시 뒷 4자리를 뒤에 더해줘야
# 뒷 4자리를 제외한 전화번호가 출력된다.

def solution(num):
    return "*" * (len(num) - 4) + num[-4:]

print(solution("01033334444"))
print(solution("027778888"))