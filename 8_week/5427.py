import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs():
    while q2:
        ci, cj = q2.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w:
                if v2[ni][nj] == 0 and arr[ni][nj] != '#':
                    q2.append([ni,nj])
                    v2[ni][nj] = v2[ci][cj] +1

    while q1:
        ci, cj = q1.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w:
                if arr[ni][nj] == '.':
                    if v1[ni][nj] == 0:
                        q1.append([ni,nj])
                        v1[ni][nj] = v1[ci][cj] +1
            else:
                return

T = int(input())
for _ in range(1,T+1):
    w, h = map(int, input().split())
    arr = [list(map(str, input()))for _ in range(h)]
    q1 = deque()
    q2 = deque()
    v1 = [[0] * w for _ in range(h)]
    v2 = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                q1.append([i,j])
                v1[i][j] = 1
            if arr[i][j] == '*':
                q2.append([i,j])
                v2[i][j] = 1
    bfs()
    mn = 1000000
    ans = 0
    for i in range(h):
        for j in range(w):
            if i== 0 or i == h-1 or j == 0 or j == w-1:
                if v1[i][j] :
                    if v2[i][j] and v2[i][j] > v1[i][j]:
                        if ans < mn:
                            ans = v1[i][j]
                            mn = ans
                    elif v2[i][j] == 0:
                        if ans < mn:
                            ans = v1[i][j]
                            mn =ans
    if ans:
        print(ans)
    else:
        print("IMPOSSIBLE")
    # for i in range(h):
    #     print(v1[i])
    # print('---')
    # for i in range(h):
    #     print(v2[i])

