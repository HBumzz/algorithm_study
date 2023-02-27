from collections import deque
dir = ((1,2), (1,-2),(-1, -2),(-1,2) ,(2,1), (2,-1), (-2,-1), (-2,1))

def bfs(ci,cj):
    global ans
    v = [[0]*N for _ in range(N)]
    v[ci][cj] = 1
    q = deque()
    q.append([ci,cj])
    while q:
        t = q.popleft()
        if t == [ti,tj]:
            ans = v[ti][tj]
            break
        for d in dir:
            ni, nj = ci+ d[0], cj + d[1]
            if 0<=ni<N and 0<=nj<N :
                ci, cj = ni, nj
                v[ni][nj] +=1
                q.append([ni,nj])
T = int(input())
for _ in range(T):
    N = int(input())
    adj = [[0]*N for _ in range(N)]
    si, sj = map(int, input().split())
    ti, tj = map(int, input().split())
    adj[ti][tj] = -1
    bfs(si,sj)
    print(ans)