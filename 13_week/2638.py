import sys
sys.stdin = open('input.txt','r')
from collections import deque
def bfs_1(si,sj):
    v = [[0]* M for _ in range(N)]
    q = deque()
    q.append([si,sj])
    v[si][sj] = 1
    arr[si][sj] = -1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni < N and 0<= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 0:
                arr[ni][nj] = -1
                q.append([ni,nj])
                v[ni][nj] = 1

N, M = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(N)]
ans = 0
while True:
    bfs_1(0, 0)
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt = 0
                for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
                    ni, nj = i+di, j+dj
                    if arr[ni][nj] == -1:
                        cnt+=1
                if cnt >= 2:
                    temp[i][j] = 1
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 1:
                arr[i][j] = -1
    ans += 1
    flag = 0
    for i in range(N):
        if flag == 1:
            break
        for j in range(M):
            if arr[i][j] == 1:
                flag = 1
                break
    if flag == 0:
        break
print(ans)