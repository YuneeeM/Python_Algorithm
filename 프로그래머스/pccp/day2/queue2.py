# 큐(Queue)
que = []
n = int(input())

for i in range(n):
    cmd = input().split()  # split은 무조건 list로 반환
    if cmd[0] == 'i':
        que.append(int(cmd[1]))
    elif cmd[0] == 'o':
        if len(que) == 0:
            print("empty")
        else:
            print(que.pop(0))
    elif cmd[0] == 'c':
        print(len(que))
