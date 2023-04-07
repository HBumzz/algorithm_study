from collections import deque
from copy import deepcopy
from itertools import combinations
N, M = map(int, input().split())

def bfs():
    while temp_q:
        ci, cj = temp_q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni < N and 0<=nj < M:
                if v[ni][nj] == 0 and arr[ni][nj] == 0:
                    temp_q.append([ni,nj])
                    v[ni][nj] = 1
    return v
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
mx = 0
cnt_1 = 0
comb = []
v1 = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            q.append([i,j])
            v1[i][j] = 1
        if arr[i][j] == 1:
            cnt_1 +=1
        if arr[i][j] == 0:
            comb.append([i,j])

combi = list(combinations(comb, 3))
for i in range(len(combi)):
    for j in combi[i]:
        ti, tj = j
        arr[ti][tj] = 1
    temp_q = deepcopy(q)
    v = deepcopy(v1)
    temp_ans = bfs()
    temp_cnt = 0
    for k in range(N):
        for l in range(M):
            if temp_ans[k][l] == 1:
                temp_cnt +=1
    ans = (N*M)- temp_cnt - cnt_1 - 3
    if ans > mx :
        mx = ans
    for j in combi[i]:
        ti, tj = j
        arr[ti][tj] = 0
print(mx)