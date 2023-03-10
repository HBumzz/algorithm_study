import sys
from collections import deque
sys.stdin = open('input.txt','r')

def bfs(start):
    global v
    v = [[[0]*col for _ in range(row)] for _ in range(level)]
    q = deque()
    for s in start:
        v[s[0]][s[1]][s[2]] = 1
        q.append(s)
    while q:
        sh,si,sj = q.popleft()
        for dh,di,dj in ((0,0,1), (0,1,0), (1,0,0),(-1,0,0),(0,0,-1),(0,-1,0)):
            nh,ni,nj = sh+dh, si+di, sj+dj
            if 0<= nh <level and 0<=ni < row and 0<= nj < col and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0:
                v[nh][ni][nj] = v[sh][si][sj] + 1
                q.append([nh,ni,nj])

def search(v): # 익지않은 토마토 처리
    global ans
    for h in range(level):
        for i in range(row):
            for j in range(col):
                if v[h][i][j] == 0 and arr[h][i][j] == 0:
                    ans = -1
                    return ans
    return ans
col, row, level = map(int, input().split())
arr = [[list(map(int,input().split())) for _ in range(row)] for _ in range(level)]
# print(arr[1]) # h,i,j 순이라 기억
# 익은 토마토 1, 익지않은 토마토 0, 토마토 없는곳 -1
start = []
for h in range(level):
    for i in range(row):
        for j in range(col):
            if arr[h][i][j] == 1:
                start.append([h,i,j])
bfs(start)
mx = 0
for h in range(level):
    for i in range(row):
        for j in range(col):
            if v[h][i][j] > mx:
                mx = v[h][i][j]
ans = mx-1
real_ans = search(v)
print(real_ans)