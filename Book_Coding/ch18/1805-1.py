# 2D 행렬 검색 2 - 첫 행의 맨 뒤에서 탐색
'''
mxn 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.
'''


def searchMatrix(self, matrix, target):
    # 예외처리
    if not matrix:
        return False

    # 첫 행의 맨 뒤
    row = 0
    col = len(matrix[0]) - 1

    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        # 타켓이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -= 1
        # 타켓이 크면 아래로 이동
        elif target > matrix[row][col]:
            row += 1

    return False
