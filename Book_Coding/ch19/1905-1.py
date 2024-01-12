# 1비트의 개수
'''
부호없는 정수형 unsigned integer을 입력받아 1비트의 개수를 출력하라
'''

print("----1의 개수 ----")


def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')


print("----비트 연산 ----")


def hammingWeight2(self, n: int) -> int:
    count = 0
    while n:
        # 1을 뺀 값과 AND 연산 횟수 측정
        n &= n-1
        count += 1
    return count
