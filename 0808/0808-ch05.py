import sys

'''
전역변수와 지역변수

main에서 선언된 변수 == 전역변수

지역변수를 우선으로 한다.
'''


def DFS1():
    cnt = 3  # 지역변수
    print(cnt)


def DFS2():
    global cnt  # 전역변수
    if cnt == 5:
        cnt = cnt+1  # 전역변수없을 때 선언 시 지역변수로 선언됨
        print(cnt)


def DFS3():
    # a[0] = 7  # 참조 -> local list를 만든게 아닌 전역 list로 인식
    a = [7, 8]  # local list
    # a = a+[4] #local list에 4를 더함? 오류남
    print(a)


if __name__ == "__main__":
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)
    a = [1, 2, 3]
    DFS3()
    print(a)
