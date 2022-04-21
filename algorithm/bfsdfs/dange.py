from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0] # 아래 밑에 왼쪽 오른쪽 탐방을 위한것

def bfs(dange,start):
    n = len(dange)
    stack = deque()
    stack.append(start)
    dange[start[0]][start[1]] = 0 # 지나간곳은 0으로 처리
    count = 1

    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dange[nx][ny] == 1:
                dange[nx][ny] = 0
                stack.append((nx,ny))
                count += 1
    return count



n = int(input())
dange = []
for i in range(n):
    dange.append(list(map(int,input())))

cnt = []
for i in range(n):
    for j in range(n):
        if dange[i][j] == 1:
            cnt.append(bfs(dange,(i,j)))
    
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])