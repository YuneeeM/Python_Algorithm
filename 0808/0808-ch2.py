import sys
from collections import deque

sys.stdin = open("0808/input2.txt", "rt")  # 파일 읽어오기

'''
이진트리 순회(깊이우선탐색: DFS)

               부모
              /     \
           왼쪽   오른쪽
-----------------------------------
 전위(VLR), 중위(LVR), 후위(LRV)
'''


def DFS(v):
    if v > 7:
        return
    else:
       # print(v, end=' ')  # 전위순위 방식
        DFS(v*2)
       # print(v, end=' ')  # 중위순위 방식
        DFS(v*2+1)
        print(v, end=' ')  # 후위순위 방식


if __name__ == "__main__":
    DFS(1)
