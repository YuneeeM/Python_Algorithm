import sys
import random as r
sys.stdin = open("0718/input1.txt", "rt")  # 파일 읽어오기

'''
이분검색
n개의 숫자가 입력으로 주어짐
n개의 수를 오름차순으로 정렬하고 다음 n개의 수 중 한 개의 수인 m이 주어지면 이분검색으로
m이 정렬된 상태에서 몇번째에 있는 지 구하기

'''

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = len(a)-1

a.sort()

while lt <= rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] < m:
        lt = mid+1
    else:
        rt = mid-1


# for i in range(len(a)):
#     if a[mid] == m:
#         print(mid+1)
#         break
#     elif a[mid] < m:
#         lt = mid+1
#         mid = (lt+rt)//2
#     else:
#         rt = mid
#         mid = (lt+rt)//2
