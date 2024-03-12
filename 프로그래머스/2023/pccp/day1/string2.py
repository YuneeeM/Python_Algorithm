# 문자수(count)
s = "You need Python"
print(s.count('o'))

# 문자 위치 찾기(index)
print(s.index('e'))
print(s.index('ed'))
# print(s.index('z'))  # valueError

# 문자 위치 찾기(find)
print(s.find('e'))
print(s.find('ed'))
print(s.find('z'))  # -1

# 문자열 삽입 (join) - 문자열을 가지고 st 데이터 사이사이를 합침
st = ['a', 'c', 'e', 't', 'y']
tt = '합치기'.join(st)

print(tt)

a = ','
print(a.join("abcd"))
print(a.join(['a', 'b', 'c', 'd']))

# 문자열 나누기 - input()무조건 문자열을 입력받음
print(s.split())
print(s.split(' '))

# 문자 입력받기
ss = list(map(int, input().split()))
