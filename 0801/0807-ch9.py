import sys
from collections import deque

sys.stdin = open("0801/input9.txt", "rt")  # 파일 읽어오기

'''
아나그램
아나그램이란 두 문자열이 알파벳의 나열 순서는 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 함
AbaAeCe와 baeeACA는 알파벳의 나열 순서는 다르지만 그 구성을 살펴보면 알파벳과 그 개수는 일치함
대소문자 구분함
'''

a = input()
b = input()

p1 = dict()
p2 = dict()


for i in a:
    p1[i] = p1.get(i, 0)+1
for i in b:
    p2[i] = p2.get(i, 0)+1

for i in p1.keys():
    if i in p2.keys():
        if p1[i] != p2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")


'''
for i in a:
    p1[i] = 0

for i in b:
    p2[i] = 0

for i in a:
    p1[i] += 1

for i in b:
    p2[i] += 1

for key, value in p1.items():
    if p2[key] == p1[key]:
        print("YES")
        break
else:
    print("NO")

'''
