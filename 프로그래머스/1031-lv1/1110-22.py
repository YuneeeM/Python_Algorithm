#크레인 인형뽑기 게임
def solution(board, moves):
    stack = []
    answer = 0

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                stack.append(board[i][m-1])
                board[i][m-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2     
                break

    return answer