#달리기 경주
def solution(players, callings):
    # 선수: 등수 딕셔너리 생성
    player_rank = {player: i for i, player in enumerate(players)}
    
    for called_player in callings:
        # 호명된 선수가 리스트에 없으면 에러 발생
        if called_player not in player_rank:
            raise ValueError(f"{called_player} is not in the player list.")
        
        current_rank = player_rank[called_player] # 호명된 선수의 현재 등수

        # 현재 등수가 0보다 크면 앞 선수와 위치를 바꿔준다.
        if current_rank > 0:
            player_in_front = players[current_rank-1] # 앞에 위치했던 선수
            
            # 등수 변경
            player_rank[called_player] -= 1
            player_rank[player_in_front] += 1 

            # 선수 위치 변경
            players[current_rank-1], players[current_rank] = players[current_rank], players[current_rank-1]
            
    return players
