# 리스트 생성하기
l1 = ['p', 'y', 't', 'h', 'o', 'n', 71, 42]
print(l1)

# 리스트 인덱스(위치), 슬라이스(시작:끝:단계)
print(l1[0])
print(l1[-1])
print(l1[3:7])
print(l1[8:3:-1])

# 리스트 연산(+,*)
print(l1+[11, 22, 33])
print(l1*3)

# 리스트 길이(len)
print(len(l1))

# 리스트 추가(append)
l1.append('hi')
