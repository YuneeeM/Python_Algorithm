# 로그인 성공?
def solution(id_pw, db):
    answer = ''
    n = len(db)
    for i in range(n):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    else:
        return "fail"
