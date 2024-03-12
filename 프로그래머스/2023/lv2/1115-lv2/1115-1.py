#최댓값과 최솟값
def solution(s):
    s = s.replace('-', ' -')
    arr = [int(x) for x in s.split()]
    return str(min(arr)) + ' ' + str(max(arr))