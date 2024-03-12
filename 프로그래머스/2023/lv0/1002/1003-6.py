# 캐릭터의 좌표
def solution(keyinput, board):
    answer = [0, 0]
    xx = board[0]
    yy = board[1]

    for x in keyinput:
        if x == "left" and answer[0]-1 >= -(xx//2):
            answer[0] -= 1
        elif x == "right" and answer[0]+1 <= (xx//2):
            answer[0] += 1
        elif x == "up" and answer[1]+1 <= (yy//2):
            answer[1] += 1
        elif x == "down" and answer[1]-1 >= -(yy//2):
            answer[1] -= 1

    return answer
