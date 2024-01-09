# 천단위 구분기호
stk = []
n = int(input())
answer = ''

# 뒤에서 부터 빼고 넣고
# 3개씩 뺄때마다 ',' 추가로 넣어주고
# 다시 위에서 부터 꺼내서 출력

num = int(input())
cnt = 0

for i in str(num)[::-1]:
    stk.append(i)
    cnt += 1
    if cnt == 3:
        stk.append(',')
        cnt = 0

while stk:
    answer += stk.pop()

if answer[0] == ',':
    answer = answer[1:]

print(answer)


# 숫자지만 문자로 해결
n1 = input()
# 스택으로 꺼내기 편하게 하기위해 리스트로 변경
n1 = list(n1)
i = 1
while len(n1):
    # 뒤에서 부터 빼고 넣고
    stk.append(n1.pop())
    # 3개씩 뺄때마다 ','를 추가로 넣어주고
    if i % 3 == 0 and i != n:
        stk.append(',')
    i += 1

# 다시 위에서 부터 꺼내서 출력
while len(stk) > 0:
    print(stk.pop(), end='')
