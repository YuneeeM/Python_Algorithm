'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())  # 문자열을 변환시킨 것은 아님
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])  # slice 젤 처음부터 2번전까지 추출
print(msg[3:5])  # 3번 4번 index 추출
print(len(msg))

# 문자 하나하나 접근
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end='')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x))  # 대문자의 아스키 넘버를 알려줌(A:65, Z:90)

tmp = 'az'
for x in tmp:
    print(ord(x))  # 대문자의 아스키 넘버를 알려줌(a:97, z:122)

tmp = 65
print(chr(tmp))  # 아스키넘버에 대응하는 문자 출력
