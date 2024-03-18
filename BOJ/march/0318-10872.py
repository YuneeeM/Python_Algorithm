# 팩토리얼 - 수학/구현

def f(n):
    if n == 0:
        return 1
    return n*f(n-1)


if __name__ == "__main__":
    n = int(input())
    print(f(n))
