# 삼총사
def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for x in range(j+1, len(number)):
                if number[i]+number[j]+number[x] == 0:
                    answer += 1

    return answer
