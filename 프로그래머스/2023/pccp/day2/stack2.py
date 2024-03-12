# 스택
stk = []
n = int(input())

for i in range(n):
    cmd = input().split()  # split은 무조건 list로 반환
    if cmd[0] == 'i':
        stk.append(int(cmd[1]))
    elif cmd[0] == 'o':
        if len(stk) == 0:
            print("empty")
        else:
            print(stk.pop())
    elif cmd[0] == 'c':
        print(len(stk))
