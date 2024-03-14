# 최댓값 - 구현
num = []

for _ in range(9):
    temp = int(input())
    num.append(temp)

max_num = max(num)
print(max_num)
print(num.index(max_num)+1)
