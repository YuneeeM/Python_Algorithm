# 문자열 반복 - 구현/문자열

n = int(input())
arr = []

for _ in range(n):
    a, b = map(str, input().split())
    arr.append((a, b))

for a, b in arr:
    for bee in b:
        print(bee*int(a), end="")
    print()

'''
for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김
'''
