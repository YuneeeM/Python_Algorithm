'''
반복문(for, while)
'''

a = range(1, 10)
print(list(a))

for i in range(10):
    print(i)

for i in range(10, 0, -1):
    print(i)

i = 1
while i <= 10:
    print(i)
    i = i+1

i = 10
while i >= 1:
    print(i)
    i = i-1

# 무한반복

i = 1
while True:
    print(i)
    i += 1

i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 11):
    print(i)
    if i > 15:
        break  # 정상종료가 아니라면 else문을 출력하지 않음
else:
    print(11)
