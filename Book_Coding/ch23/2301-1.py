#피보나치 수 - 재귀 구조 브루트 포스

def fib(self, N:int) -> int:
    if N <=1:
        return N
    return self.fib(N-1) + self.fib(N-2)