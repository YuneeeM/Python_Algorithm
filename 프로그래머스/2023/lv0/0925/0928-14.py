# 인덱스 바꾸기
def solution(my_string, num1, num2):
    arr = []
    for x in my_string:
        arr.append(x)

    arr[num1], arr[num2] = arr[num2], arr[num1]

    my_string = ""

    for x in arr:
        my_string += x

    return my_string
