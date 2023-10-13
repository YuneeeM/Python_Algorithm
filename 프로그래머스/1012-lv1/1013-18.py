# 핸드폰 번호 가리기
def solution(phone_number):
    answer = ''
    phone_number = [x for x in str(phone_number)]
    for i in range(len(phone_number)-4):
        phone_number[i] = "*"
    return "".join(phone_number)
