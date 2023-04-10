# ㅈㄴ어렵넹ㅋ

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(ci,cj):
    if v[ci][cj]:
        return v[ci][cj]
    v[ci][cj] = 1
    for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni, nj = ci+di, cj+dj
        if 0<= ni < N and 0<= nj < N and arr[ni][nj] > arr[ci][cj] :
            v[ci][cj] = max(v[ci][cj], dfs(ni,nj) + 1)
    return v[ci][cj]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0]*N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans,dfs(i,j))

print(ans)