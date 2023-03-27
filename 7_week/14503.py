N, M = map(int, input().split())
si, sj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = [[-1,0], [0,1], [1,0], [0,-1]]
cnt = 0
if arr[si][sj] == 0:
    arr[si][sj] = 1
    cnt += 1
while True:
    for di, dj in dir:
        ni, nj = si+di, sj+dj
        if 0<=ni < N and 0<= nj < M and arr[ni][nj] == 1:
