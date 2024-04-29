'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x)
print()

b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7 튜플은 값을 변경할 수 없음
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()


if all(50 > x for x in a):  # 모두
    print("YES")
else:
    print("NO")

if any(50 > x for x in a):  # 하나라도 참
    print("YES")
else:
    print("NO")
