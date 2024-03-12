# 2017 연세대학교 프로그래밍 경시대회

N = int(input())

res = 0

for A in range(0, N+1):
    for B in range(0, N+1):
        for C in range(0, N+1):
            if A+B+C == N:
                if C >= B+2:
                    if A != 0 and B != 0 and C != 0:
                        if A % 2 == 0:
                            res += 1

print(res)
