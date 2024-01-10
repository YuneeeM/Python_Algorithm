# 2D 행렬 검색 2 - 파이썬다운 방식
'''
mxn 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.
'''


def searchMatrix(self, matrix, target):
    return any(target in row for row in matrix)
