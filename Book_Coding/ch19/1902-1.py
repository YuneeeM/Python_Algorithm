# 해밍거리 - XOR 풀이
'''
두 정수를 입력받아 몇 비트가 다른지 계산하라.
'''


def hammingDistance(self, x: int, y: int) -> int:
    return bin(x ^ y).count('1')
