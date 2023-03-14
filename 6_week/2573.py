import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
day = 0
check = False
q = deque()
di, dj = [-1,1,0,0], [0,0,-1,1]

def bfs(i,j):
    q.append((i,j))
    while q:
        ci,cj = q.popleft()
        visited[ci][cj] = 1
        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] != 0 and visited[ni][nj] == False:
                    visited[ni][nj] = True
                    q.append((ni,nj))
                elif arr[ni][nj] == 0:
                    count[ci][cj] += 1
    return 1

while True:
    result = []
    visited = [[0] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0:
                result.append(bfs(i,j))

    for i in range(N):
        for j in range(M):
            arr[i][j] -= count[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    day +=1

if check:
    print(day)
else:
    print(0)