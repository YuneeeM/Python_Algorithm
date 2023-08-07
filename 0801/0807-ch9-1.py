import sys
from collections import deque

sys.stdin = open("0801/input9.txt", "rt")  # 파일 읽어오기

a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0)+1

for x in b:
    sH[x] = sH.get(x, 0)-1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
