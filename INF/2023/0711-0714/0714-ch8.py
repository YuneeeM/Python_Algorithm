import sys
import random as r
sys.stdin = open("0711-0712/input6.txt", "rt")  # 파일 읽어오기

'''
뒤집은 소수
n개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하시오
예를 들면 32를 뒤집으면 23, 이는 소수임
그러면 소수를 출력함 910을 뒤집으면 19로 숫자화
def reverse(x) 와 소수 확인 def isPrime(X)를 사용하자
'''


def reverse(x):
    res = 0
    while (x > 0):
        t = x % 10
        res = res * 10 + t
        x = x//10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
str = list(map(int, input().split()))


for i in str:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=" ")
