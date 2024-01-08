# 문자열

# 표현방법
s1 = "hello"
s2 = 'hi'
s3 = """welcome
python"""
print(s1)
print(s2)
print(s3)

# 이스케이프 문자(\+문자 = 기능문자)
print("이\n스\\케\'이\"프\000문자")

# 문자열 연산(+,*)
print("hello"+"python")
print("hi"*3)

# 문자열 길이(len)
print(len("hello"))
print(len("hello"*3))

# 문자열 인덱스(위치), 슬라이스(시작:끝:단계)
s = "You need Python"
print(s[0], s[4])
print(s[-1], s[-4])
