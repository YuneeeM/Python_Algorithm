
import sys
sys.stdin = open("0711/input.txt", "rt")  # 파일 읽어오기


'''
K번째 약수
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
'''

K, N = map(int, input().split())

count = 0

for i in range(1, K+1):
    if K % i == 0:
        count += 1
        if count == N:
            print(i)

if count < N:
    print(-1)

'''
* 풀이과정 *

for i in range(1,K+1):
    if K%i==0:
        count+=1
    if count == N:
        print(i)
        break
else:
    print(-1) #break걸렸을 때 for-else를 사용할 수 있음
'''
