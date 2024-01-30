# 쿼드압축 후 개수 세기
def solution(arr):
    answer = [0, 0]
    leng = len(arr)

    def compression(a, b, l):
        st = arr[a][b]  # 해당 네모값중 하나 # 모두 같아야 통과임
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[i][j] != st:  # 한번이라도 다르면 그 네모드 압축 불가
                    # 4분할
                    l = l//2
                    compression(a, b, l)  # 왼쪽위
                    compression(a, b+l, l)  # 오른쪽위
                    compression(a+l, b, l)  # 왼쪽아래
                    compression(a+l, b+l, l)  # 오른쪽아래
                    return
        # 전부 통과한 경우 압축
        answer[st] += 1
    compression(0, 0, leng)

    return answer
