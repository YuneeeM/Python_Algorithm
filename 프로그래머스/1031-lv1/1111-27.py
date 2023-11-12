#공원 산책
def solution(park, routes):
  
    x, y, w, h = 0, 0, len(park[0]), len(park)
    dis = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}

    for i in range(h):
        for j in range(w):
            if park[i][j]=="S":
                x, y = i, j
                break
        
    
    for r in routes:
        d, num = r.split(" ") 
        dx, dy = x, y  
        
        for i in range(int(num)):
            nx = x + dis[d][0]
            ny = y + dis[d][1]
        
            if 0<=nx<=h-1 and 0<=ny<=w-1 and (park[nx][ny]!="X"):
                x, y = nx, ny
                    
            else:
                x, y = dx, dy
                break

    return (x,y)