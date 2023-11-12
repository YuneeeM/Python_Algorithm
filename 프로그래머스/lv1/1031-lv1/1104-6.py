#소수 만들기
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer=0
    
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for m in range(j+1,len(nums)):
                if isPrime(nums[i]+nums[j]+nums[m]):
                    answer+=1
    return answer