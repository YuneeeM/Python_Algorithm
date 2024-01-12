# [PCCP 모의고사 #1] 1번 - 외톨이 알파벳
def solution(input_string):
    answer = ''
    # 첫번째 와 두번째 데이터가 같은지 물어봄요
    # i i+1 검색을 위해 문자뒤에 ' '를 붙여주고 시작
    input_string += ' '

    # 체크를 하면서 중복 제거를 확인하기 위한 빈 set 함수
    # 외톨이 문자(중복으로 넣으면 되지 않아서 때문에 set())
    temp = set()

    # 기존문자인가?
    al = set()

    # 완전 탐색
    for i in range(len(input_string)-1):
        # 연속적인지 판단
        # 연속이 끊어지면 새로운 글자를 발견
        if input_string[i] != input_string[i+1]:
            # 새로운 문자가 발견이 되면 넣어주고
            if input_string[i] not in al:
                al.add(input_string[i])
            else:  # 아니면 외톨이 문자갇 됨
                temp.add(input_string[i])

    if len(temp) == 0:
        answer = 'N'
    else:
        temp = list(temp)
        temp.sort()
        answer = ''.join(temp)

    return answer
