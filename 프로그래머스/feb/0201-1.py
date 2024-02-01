#하노이의 탑

def solution(n):
    answer = []
    
    def hanoi(start, end, temp, n): 
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(start,temp,end,n-1)
            hanoi(start,end,temp,1)
            hanoi(temp,end,start,n-1)
            
    hanoi(1,3,2,n)
    
    return answer