import sys

sys.stdin = open("0811/input6.txt", "rt")  # 파일 읽어오기

'''
알파코드(DFS)
비밀편지를 암호화해서 서로 주고 받기
A:1, B:2 ... Z:26
'''


def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i % 10:
                res[P] = i
                DFS(L+2, P+1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0]*(n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
