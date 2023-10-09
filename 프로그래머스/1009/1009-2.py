# 이진수 더하기
def solution(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    answer = bin(num1+num2)
    answer = answer.replace("0b", "")
    return answer
