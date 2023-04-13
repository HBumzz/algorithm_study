from collections import deque
def bfs(si,sj):
    v = [[1e8]* N for _ in range(N)]
    v[si][sj] = arr[si][sj]
    q = deque()
    q.append([si,sj])
    while q:
        ci, cj = q.popleft()
        for di, dj in ((1,0),(0,1),(0,-1),(-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N:
                if v[ni][nj] > v[ci][cj] + arr[ni][nj]: # 이전 경로가 더 크다
                    v[ni][nj] = v[ci][cj] + arr[ni][nj]
                    q.append([ni,nj])
    return v[N-1][N-1]
i = 0
while True:
    i += 1
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(0,0)
    print(f'Problem {i}: {ans}')