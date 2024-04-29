'''
함수 만들기

#함수는 main script 위쪽에 작성하자
def add(a, b):
    c = a+b
    print(c)


add(3, 2)
add(5, 7)

def add(a, b):
    c = a+b
    return c

print(add(3, 2))

def add(a, b):
    c = a+b
    d = a-b
    return c, d #튜플 형태로 반환


print(add(3, 2))

'''

# 리스트에 저장된 값을 소수인지 판별하는 함수구하기


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]

for x in a:
    if isPrime(x):
        print(x, end=' ')
print()
