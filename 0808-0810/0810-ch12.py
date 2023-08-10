import sys
import itertools as it

sys.stdin = open("0808/input9.txt", "rt")  # 파일 읽어오기

'''
수열 추측하기 - 라이브러리를 이용한
가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있음

3 1 2 4
 4 3 6
  7 9
  16
  
'''


n, f = map(int, input().split())
b = [1]*n
cnt = 0
for i in range(1, n):
    b[i] = b[i-1]*(n-i)//i
a = list(range(1, n+1))


for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x*b[L])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break

# for tmp in it.permutations(a):  # 수열 경우의 수 4!
#     print(tmp)

# cnt = 0
# for tmp in it.permutations(a, 3):  # 수열의 경우의 수 3개로 4p3
#     print(tmp)
#     cnt += 1
# print(cnt)
