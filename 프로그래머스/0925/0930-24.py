# OX퀴즈
def solution(quiz):
    answer = []
    for x in quiz:
        x = x.split()
        sum = int(x[0])
        for i in range(len(x)):
            if x[i] == "+":
                sum += int(x[i+1])

            elif x[i] == "-":
                sum -= int(x[i+1])
        if sum == int(x[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer
