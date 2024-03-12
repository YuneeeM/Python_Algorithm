# 숫자 문자열과 영단어
def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']
    s = [x for x in str(s)]
    x = []
    current = ""

    for char in s:
        if char.isalpha():
            current += char
            if current in num:
                x.append(str(num.index(current)))
                current = ""
        else:
            x.append(str(char))

    return int(''.join(x))
