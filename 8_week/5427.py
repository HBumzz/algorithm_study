import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs():
    while q2: # 불에 대한 queue가 존재한다면
        ci, cj = q2.popleft() # popleft를 해서 불의 좌표를 뽑아주고
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)): # 동서남북 4방향에 관해서 돌려 줌
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w: # arr 배열을 벗어나지 않고
                if v2[ni][nj] == 0 and arr[ni][nj] != '#': # 방문하지않았고, 벽이 아니라면
                    q2.append([ni,nj]) # q2에 append 해주고
                    v2[ni][nj] = v2[ci][cj] +1 # 기존 ci,cj의 visit배열 값에 +1 을 해줌

    while q1: # 상근이에 대한 bfs인데 위 과정과 비슷함
        ci, cj = q1.popleft()
        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w:
                if arr[ni][nj] == '.':
                    if v1[ni][nj] == 0:
                        q1.append([ni,nj])
                        v1[ni][nj] = v1[ci][cj] +1
            else: # 단 arr의 범위를 벗어나는 순간 return 하면서 함수 종료
                return

T = int(input())
for _ in range(1,T+1):
    w, h = map(int, input().split())
    arr = [list(map(str, input()))for _ in range(h)] # arr 생성
    q1 = deque() # 상근이에 대한 queue인 q1과
    q2 = deque() # 불에 대한 queue인 q2를 생성
    v1 = [[0] * w for _ in range(h)] # 똑같이 상근이에대한 visit배열과
    v2 = [[0] * w for _ in range(h)] # 불에대한 visit배열을 따로 생성
    for i in range(h):
        for j in range(w): # 배열을 돌면서
            if arr[i][j] == '@': # 상근이인 @가 나오면 q1에 append를 해주고
                q1.append([i,j])
                v1[i][j] = 1 # 상근이 방문표시
            if arr[i][j] == '*': # 불인 *이 나오면 q2에 append를 해주고
                q2.append([i,j])
                v2[i][j] = 1 # v2에 불 방문표시
    bfs() # bfs함수 실행
    mn = 1000000 # min값 설정
    ans = 0 # 답에 쓰일 ans를 초기화 0에서 갱신이 안된다면 impossible이 됨
    for i in range(h):
        for j in range(w): # 상근이의 visit 배열인 v1을 돌면서
            if i== 0 or i == h-1 or j == 0 or j == w-1: # 모서리인 부분에
                if v1[i][j] : # 좌표 i,j에 대한 v1의 값이 존재하면서
                    if v2[i][j] and v2[i][j] > v1[i][j]: # i,j에 대한 v2값이 존재하고, v2[i][j] 가 v1[i][j] 보다 크다면
                        if ans < mn: # 또한 ans가 mn값보다 작으면 갱신
                            ans = v1[i][j]
                            mn = ans
                    elif v2[i][j] == 0: # v1[i][j]가 존재하는데 v2[i][j] 가 0이라면 불이 도달하지 못하는 곳이므로
                        if ans < mn: # 똑같이 ans를 갱신
                            ans = v1[i][j]
                            mn =ans
    if ans: # ans가 0이 아니라면
        print(ans) # 갱신해준 ans값 출력
    else: # 없다면 IMPOSSIBLE 출력
        print("IMPOSSIBLE")
    # for i in range(h):
    #     print(v1[i])
    # print('---')
    # for i in range(h):
    #     print(v2[i])

