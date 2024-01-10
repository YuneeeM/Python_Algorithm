# 'O', 'X'의 모든경우의수만들기
def f(cnt, st):  # 실행횟수, 가지고 다니는 문자열
    # 만약 원하는 조건이 맞으면
    # 원하는 결과를 출력한다.
    if cnt == 0:
        print(st)
        return
    f(cnt-1, st+'O')
    f(cnt-1, st+'X')


n = int(input())

f(n, "")

print("----------------------------")

# 입력과 출력, 함수를 자유롭게 작성해주세요


def f(cnt, st):  # 실행횟수, 가지고 다니는 문자열
    if cnt == 0:
        print(st)
        return
    sti = "OX"
    for i in sti:
        f(cnt-1, st+i)


n = int(input())

f(n, "")
