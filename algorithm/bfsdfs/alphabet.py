# 상,하,우,좌
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS():
    answer = 1
    queue = set([(0,0,alphabets[0][0])])

    while queue:
        x,y,visited = queue.pop()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < r and 0 <= ny < c and alphabets[nx][ny] not in visited:
                next_visited = visited + alphabets[nx][ny]
                queue.add((nx,ny,next_visited))
                answer = max(answer,len(next_visited))
    
    return answer



r,c = map(int,input().split(' '))
alphabets = []
for i in range(r):
    info = [j for j in input()]
    alphabets.append(info)

print(BFS())