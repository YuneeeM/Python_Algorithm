# 잠꼬대 영단어

def solution(words):
    answer = 0
    word = [x for x in words.split(' ')]
    word = set(word)
    answer = len(word)
    return answer


def solution2(words):
    answer = 0
    # 스페이스로 문자를 나누고
    words = words.split(' ')
    # 중복을 제거하고
    words = set(words)

    # 개수를 구함
    answer = len(words)

   # 한 줄 코딩
    return len(set(words.split(' ')))
