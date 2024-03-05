# 수들의 합

s = int(input())
sum = 0
cnt = 0
while True:
    if s > sum:
        sum += 1
        s = s-sum
        cnt += 1
    else:
        print(cnt)
        break
