#옹알이 (2)

def solution(babbling):
    result = 0
    for i in babbling:
        cnt = 0
        word = ''
        prev_word = ''
        for j in i:
            word += j
            if word in ['aya', 'ye', 'woo', 'ma']:
                if word == prev_word:
                    prev_word= word
                    cnt-=1
                else:
                    prev_word = word
                    word = ''
                    cnt += 1
        if len(word) == 0 and cnt > 0:
            result += 1
    return result
