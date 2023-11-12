# 2016년
def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = ''
    res = 0
    for i in range(a-1):
        res += months[i]

    res += b
    res = res % 7

    answer += days[res-1]

    return answer
