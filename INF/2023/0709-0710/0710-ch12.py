'''
람다함수 (익명의 함수 ? 표현식? )
'''


def plus_one(x):
    return x+1


print(plus_one(1))


#plus_two = lambda x : x+2

# print(plus_two(1))

a = [1, 2, 3]
print(list(map(plus_one, a)))  # map에서 전자는 함수명, 후자는 변수

print(list(map(lambda x: x+1, a)))  # 인자로 바로
