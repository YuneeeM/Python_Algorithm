#가장 큰 수
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))               
    numbers.sort(key = lambda x : x*3,reverse=True)  
    
    for x in numbers:             
        answer += x
    
    return str(int(answer))