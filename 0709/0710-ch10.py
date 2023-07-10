'''
2차원 리스트 생성과 접근

a = [0]*3
print(a)

'''

a = [[0]*3 for _ in range(3)]
print(a)
a[0][1] = 1
print(a)
a[1][1] = 1
print(a)

for x in a:
    print(x)
print()

for x in a:
    for j in x:
        print(j, end=' ')
    print()
print()
