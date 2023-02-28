import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(ci,cj):
    global cnt
    v = [[[0]*M for _ in range(N)] for _ in range(2)]
    v[0][ci][cj] = 1
    v[1][ci][cj] = 1
    q = deque()
    q.append([0,ci,cj])
    while q:
        cnt, ci, cj = q.popleft()
        for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and v[cnt][ni][nj] == 0 and cnt == 0 and arr[ni][nj] == 1:
                v[1][ni][nj] = v[cnt][ci][cj]+1
                q.append([1,ni,nj])
            elif 0<=ni<N and 0<=nj<M and v[cnt][ni][nj] == 0 and arr[ni][nj] == 0:
                v[cnt][ni][nj] = v[cnt][ci][cj]+1
                q.append([cnt, ni, nj])
    return v

N, M = map(int, input().split())
arr = [list(map(int , input())) for _ in range(N)]
si, sj = 0, 0
ans = bfs(si,sj)
if ans[cnt][N-1][M-1] == 0:
    ans = -1
else:
    ans = ans[cnt][N-1][M-1]
print(ans)