#둘만의 암호
def solution(s, skip, index):
    string = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for x in list(skip):
        string = string.replace(x,"")
        
    for x in s:
        answer += string[(string.find(x) + index) % len(string)]
    return answer