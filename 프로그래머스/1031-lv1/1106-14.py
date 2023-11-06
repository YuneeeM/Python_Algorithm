from collections import Counter

def solution(X, Y):
    X_digits = Counter(str(X))
    Y_digits = Counter(str(Y))

    common_digits = X_digits & Y_digits

    if common_digits:
        common_digits_list = list(''.join([k * v for k, v in common_digits.items()]))
        common_digits_list.sort(reverse=True)
        # 0으로 시작하는 숫자를 처리
        if common_digits_list[0] == '0':
            return '0'
        else:
            return ''.join(common_digits_list)
    else:
        return '-1'
