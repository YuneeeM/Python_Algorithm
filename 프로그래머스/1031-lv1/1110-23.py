#키패드 누르기
def dis(lr, key): #현재 왼손,오른손 의 위치와 key를 입력
    pos = {
        '*': (3, 0),
        '#': (3, 2),
        '1': (0, 0),
        '2': (0, 1),
        '3': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (2, 0),
        '8': (2, 1),
        '9': (2, 2),
        '0': (3, 1),
    }
    leftRight = pos[lr]
    Key = pos[key]
    return abs(leftRight[0] - Key[0]) + abs(leftRight[1] - Key[1])

def solution(numbers, hand):
    numbers = [str(x) for x in numbers]
    left, right = '*', '#'
    answer = []
    for x in numbers:
        if x in '147':
            answer.append('L')
            left = x
        elif x in '369':
            answer.append('R')
            right = x
        else:
            if dis(left, x) < dis(right, x):
                answer.append('L')
                left = x
            elif dis(right, x) < dis(left, x):
                answer.append('R')
                right = x
            else:
                if hand == 'left':
                    answer.append('L')
                    left = x
                else:
                    answer.append('R')
                    right = x
    
    return ''.join(answer)