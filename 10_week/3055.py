from collections import deque
def bfs1(): # 도치
    global ans
    ans = []
    while q1:
        ci, cj = q1.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<= ni< N and 0<= nj < M and v1[ni][nj] == 0 and arr[ni][nj] != 'X':
                v1[ni][nj] = v1[ci][cj] +1
                q1.append([ni,nj])
            if ni == ei and nj == ej:
                ans.append([ci,cj,v1[ci][cj]])

def bfs2(): # 물
    global ANS
    ANS = []
    while q2:
        ci, cj = q2.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<= ni< N and 0<= nj < M and v2[ni][nj] == 0 and arr[ni][nj] == '.':
                v2[ni][nj] = v2[ci][cj] +1
                q2.append([ni,nj])
            if ni == ei and nj == ej:
                ANS.append([ci,cj,v2[ci][cj]])


N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
q1 = deque() # 도치
q2 = deque() # 물
v1 = [[0]* M for _ in range(N)]
v2 = [[0]* M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'D':
            ei, ej = i, j
        if arr[i][j] == 'S':
            si, sj = i, j
            q1.append([si,sj])
            v1[si][sj] = 1
        if arr[i][j] == '*':
            Si, Sj = i, j
            q2.append([Si,Sj])
            v2[Si][Sj] = 1
bfs1()
bfs2()
print(ans, ANS)
r_ans = 2500
if len(ans) <= len(ANS):
    for i in ans:
        for j in ANS:
            if i[0] == j[0] and i[1] == j[1]:
                if i[2] < j[2]:
                    r_ans = min(r_ans, i[2])
else:
    k = 0
    while ANS:
        a = ANS.pop()
        for i in ans:
            if i[0] == a[0] and i[1] == a[1]:

if r_ans == 2500:
    print('KAKTUS')
else:
    print(r_ans)