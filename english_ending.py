# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

# 처음에 strg변수에 가장 첫 단어를 넣어준다. 그리고 for문으로 두번째 단어부터 단어의 전체 길이만큼 돌아주고,
# 끝말잇기가 제대로 돌 수 있는지 확인한다. 불가능한 경우는 제시한대로 2가지 이므로 첫 번째 불가능한 경우를 넣어주고,
# 불가능 할 시에 번호를 나타내는 num 값을 계산해 넣어주고, count에 차례를 계산해 넣어준다.
# 그 if문 안에서 또 한번 불가능한 경우와 가능한 경우에 대해 계산을 해준 뒤 빠져나와
# 주어진 단어 모두 탈락자가 생기지 않는 경우를 넣어주고, 마지막에 count 값과 n의 값을 계산해 answer에 리스트로 넣어준 뒤
# return한다.

def solution(n, words):
    strg = [words[0]]
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]:
            num = i % n + 1
            count = i + 1
            break
        else:
            if words[i] not in strg:
                strg.append(words[i])
            else:
                num = i % n + 1
                if num == 0:
                    num = n
                count = i + 1
                break
    else:
        return [0, 0]
    if count % n == 0:
        count //= n
    else:
        count = count // n + 1
    answer = [num, count]
    return answer


def test_solution():
    assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3, 3]
    assert solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0, 0]
    assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]