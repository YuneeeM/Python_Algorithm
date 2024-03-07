# ATM - 그리디 알고리즘/정렬
n = int(input())
p = list(map(int, input().split()))

p.sort()

answer = 0
temp = 0

for pi in p:
    temp += pi
    answer += temp

'''
for x in range(1,n+1):
    answer+=sum(p[0:x])
'''

print(answer)
