# 별 찍기 - 10
n = int(input())


def stars(n):
    if n == 1:
        return ['*']

    S = stars(n//3)

    arr = []

    for star in S:
        arr.append(star*3)
    for star in S:
        arr.append(star+' '*(n//3)+star)
    for star in S:
        arr.append(star*3)

    return arr


print('\n'.join(stars(n)))
