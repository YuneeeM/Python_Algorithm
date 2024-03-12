# A로 B만들기
def solution(before, after):
    answer = 0
    # 전 후 모두 리스트로 변경 후 정렬, 그리고 비교
    before = list(before)
    after = list(after)

    before.sort()
    after.sort()

    for i in range(len(before)):
        if before[i] != after[i]:
            return 0

    '''
    if before == after:
      answer = 1
    else:
      answer = 0

    가능 - 리스트는 통째로 비교가 가능하다
    '''
    return 1
