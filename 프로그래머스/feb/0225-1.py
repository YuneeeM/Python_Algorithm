# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    participant_dict = {}
    
    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1
    
    for c in completion:
        participant_dict[c] -= 1
    
    for p, count in participant_dict.items():
        if count > 0:
            answer = p
            break
    
    return answer
