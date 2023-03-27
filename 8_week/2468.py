import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input.txt','r')

def bfs(si,sj):
    global ans
    q = deque()
    q.append([si,sj])
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj + dj
            if 0<=ni < N and 0<=nj<N and arr[ni][nj] !=0 and v[ni][nj] == 0:
                v[ni][nj] = 1
                arr[ni][nj] = 0
                q.append([ni,nj])
    ans +=1
N = int(input())
arr_origin = [list(map(int, input().split())) for _ in range(N)]
mx = 0
for i in range(N):
    if max(arr_origin[i]) > mx:
        mx = max(arr_origin[i])
lst = [x for x in range(0,mx+1)]
ans_lst = []
for rain in lst:
    arr = deepcopy(arr_origin)
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                arr[i][j] = 0
    ans = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                bfs(i,j)
    ans_lst.append(ans)
print(max(ans_lst))
