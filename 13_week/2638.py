import sys
sys.stdin = open('input.txt','r')
from collections import deque
def bfs_1(si,sj):
    v = [[0]* M for _ in range(N)]
    q = deque()
    q.append([si,sj])
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni < N and 0<= nj < M and v[ni][nj] == 0:
                if arr[ni][nj] >= 1:
                    arr[ni][nj] += 1
                else:
                    v[ni][nj] = 1
                    q.append([ni,nj])
N, M = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(N)]
time = 0
while True:
    flag = 0
    bfs_1(0, 0)
    for i in range(N):
        for j in range(M):
            if arr[i][j] >=3:
                arr[i][j] = 0
                flag = 1
            elif arr[i][j] == 2:
                arr[i][j] =1
    if flag == 1:
        time+=1
    else:
        break
print(time)