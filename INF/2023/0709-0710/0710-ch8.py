'''
리스트와 내장함수(1)
'''
import random as r

a = []
# print(a)
b = list()
# print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b = list(range(1, 11))
# print(b)

c = a+b
# print(c)


print(a)
a.append(6)  # 추가
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)
a.pop(3)  # index의 값을 빠지게 해라
print(a)

a.remove(4)  # value를 제거해라
print(a)

print(a.index(5))  # 5값이 어디있는지 index번호 반환

a = list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7, 3, 5))  # 인자값중에 최솟값을 찾아줌
print(a)
r.shuffle(a)  # 무작위 섞기
print(a)

a.sort()  # 오름차순
print(a)
a.sort(reverse=True)  # 내림차순
print(a)
a.clear()  # 리스트 비우기
print(a)
