# K번째수
def solution(array, commands):
    answer = []
    for s, e, k in commands:
        subarray = sorted(array[s-1:e])
        answer.append(subarray[k-1])  
    return answer