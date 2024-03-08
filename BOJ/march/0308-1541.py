# 잃어버린 괄호 - 그리디 알고리즘

res = input().split('-')

exp = []

for r in res:
    psum = 0
    temp = r.split('+')
    for t in temp:
        psum += int(t)
    exp.append(psum)

st = exp[0]

for i in range(1, len(exp)):
    st -= exp[i]

print(st)
