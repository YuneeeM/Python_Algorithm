# day 1 복습
# 1 - string (qrcode)
print("--------------------------------------------------")


def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer


# 2 - string (크기가 작은 부분문자열)
print("--------------------------------------------------")


def solution2(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer


# 3 - string (문자열 겹쳐쓰기)
print("--------------------------------------------------")


def solution(my_string, overwrite_string, s):

    answer = my_string[:s] + overwrite_string + \
        my_string[s+len(overwrite_string):]
    return answer


# 4 - string (반지)
print("--------------------------------------------------")


def solution(wordfind, N, ring):
    answer = 0
    for i in ring:
        if wordfind in i*2:
            answer += 1
    return answer


# 6 - array (n개 간격의 원소)
print("--------------------------------------------------")


def solution(num_list, n):
    answer = num_list[::n]
    return answer


# 7 - array (자연수 뒤집어 배열로 만들기)
print("--------------------------------------------------")


def solution(n):
    answer = [int(x) for x in str(n)]
    return answer[::-1]


def s(n):
    answer = 0
    n = str(n)
    n = list(n)
    n = n[::-1]
    answer = list(map(int, n))
    return answer


def s1(n):
    return list(map(int, str(n)))[::-1]


# 8 - hash (빼빼로 데이)
print("--------------------------------------------------")


def solution(pepero):
    answer = list(set(pepero))
    answer.sort()
    return answer


# 9 - hash (잠꼬대영단어)
print("--------------------------------------------------")


def solution(words):
    answer = 0
    word = [x for x in words.split(' ')]
    word = set(word)
    answer = len(word)
    return answer


# 10 - hash (모스부호(1))
print("--------------------------------------------------")


def solution(letter):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    answer = ''
    for x in letter.split(' '):
        if x in morse:
            answer += morse[x]
    return answer


# 11 - hash (완주하지 못한 선수들)
print("--------------------------------------------------")


def solution(participant, completion):
    answer = ''
    dict = {}
    for p in participant:
        dict[p] = dict.get(p, 0)+1
    for c in completion:
        dict[c] -= 1

    for k, v in dict.items():
        if v > 0:
            answer += k
    return answer


def solution2(participant, completion):
    answer = ''
    part = {}
    for i in participant:
        if i in part:
            part[i] += 1
        else:
            part[i] = 1
    for i in completion:
        if part[i] == 1:
            del part[i]
        else:
            part[i] -= 1
    answer = list(part)

    return answer[0]


def solution3(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]

    return participant[-1]


# 12 - sort (A로 B 만들기)
print("--------------------------------------------------")


def solution(before, after):
    answer = 0
    before = list(before)
    after = list(after)

    for i in range(len(before)):
        if before[i] != after[i]:
            return 0
    return 1
