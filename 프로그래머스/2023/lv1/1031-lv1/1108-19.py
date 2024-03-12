#대충 만든 자판
def solution(keymap, targets):
    answer=[]
    keymap_dict = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            key = keymap[i][j]
            if key not in keymap_dict:
                keymap_dict[key] =(j + 1)
            else:
                keymap_dict[key] = min(keymap_dict[key],(j + 1))
    
    for temp in targets:
        sum=0
        for x in temp:
            if x in keymap_dict:
                sum += keymap_dict[x]
            else:
                sum = -1
                break
        answer.append(sum)
    return answer