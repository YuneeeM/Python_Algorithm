# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
arr = [a*('*') for _ in range(b)]
for x in arr:
    print(x)
