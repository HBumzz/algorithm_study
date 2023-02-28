import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs(ci,cj):
    global ans
    v[ci][cj] = 1
    q = deque()
    q.append([ci,cj])
    while q:
        ci, cj = q.popleft()
        if ci == ti and cj == tj:
            ans = v[ci][cj]-1
            return ans
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append([ni,nj])

T = int(input())
dir = ((1,2), (1,-2),(-1, -2),(-1,2) ,(2,1), (2,-1), (-2,-1), (-2,1))
for test_case in range(T):
    N = int(input())
    v = [[0]* N for _ in range(N)]
    si, sj = map(int, input().split())
    ti, tj = map(int, input().split())
    print(bfs(si,sj))