# 블랙잭 - 브루트 포스
n, m = map(int, input().split())
black = list(map(int, input().split()))

answer = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            res = black[i]+black[j]+black[k]
            if res > m:
                continue
            else:
                answer.append(res)

print(max(answer))
