import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs():
    while q2:
        ci, cj = q2.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v2[ni][nj] == 0 and arr[ni][nj] != '#':
                q2.append([ni,nj])
                v2[ni][nj] = v2[ci][cj] +1

    while q1:
        ci, cj = q1.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '.' and v1[ni][nj] == 0:
                    q1.append([ni, nj])
                    v1[ni][nj] = v1[ci][cj] + 1


N, M = map(int, input().split())

v1 = [[0]* M for _ in range(N)]
v2 = [[0]* M for _ in range(N)]
q1 = deque()
q2 = deque()
arr = [list(map(str, input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'J':
            q1.append([i,j])
            v1[i][j] = 1
        if arr[i][j] == 'F':
            q2.append([i,j])
            v2[i][j] = 1
bfs()
ans = 0
mn = 1000000
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            if v1[i][j]:
                if v2[i][j] and v1[i][j] < v2[i][j]:
                    if v1[i][j] < mn:
                        ans = v1[i][j]
                        mn = ans
                elif not v2[i][j]:
                    if v1[i][j] < mn:
                        ans = v1[i][j]
                        mn = ans
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')
for i in range(N):
    print(v1[i])
print('------------')
for i in range(N):
    print(v2[i])