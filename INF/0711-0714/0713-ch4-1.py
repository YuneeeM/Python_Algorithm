'''
대표값 문제 오류 수정
round는 round_half_even방식을 택한다.

'''

a = 4.500
print(round(a))
# 정확한 4.5에 있으면 짝수쪽으로 간다는 의미로 4택함

a = 4.511
print(round(a))

b = 66.5
b = b+0.5
b = int(b)
print(b)
