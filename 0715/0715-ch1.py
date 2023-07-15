import sys
import random as r
sys.stdin = open("0715/input1.txt", "rt")  # 파일 읽어오기

'''
회문 문자열 검사

n개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면
yes 출력 회문 문자열이 아니면 no를 출력하는 프로그램
대소문자 구분은 안함
'''

n = int(input())


for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("# %d No" % (i+1))
            break

    else:
        print("# %d YES" % (i+1))

    # if s == s[::-1]: 더 간단한 방법!
    #     print("YES")
    # else:
    #     print("NO")
