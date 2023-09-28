# 인덱스 바꾸기
def solution(numbers):
    arr = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
    for k, v in enumerate(arr):
        numbers = numbers.replace(v, str(k))

    return int(numbers)


'''
def solution(numbers):
    answer = 0
    arr=["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for x in arr:
        if x in numbers:
            answer=answer*10+arr.index(x)
        
    return answer

0을 인식 못해서 위 방법으로 해결함
'''
