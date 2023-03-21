
def dfs(si,sj,pi,pj,cnt,color):
    global ans
    if ans == 1: # ans가 1이라면 싸이클이 존재하기 때문에 함수 종료
        return
    for di, dj in ((0,-1), (-1,0), (0,1), (1,0)):
        ni, nj = si+di, sj+dj # 동서남북 방향으로 이동방향 설정
        if 0<= ni < N and 0<= nj <M: # 이동방향이 범위를 벗어나지 않고
            if cnt>=4 and ni == pi and nj == pj : # cnt가 4이상이면서 ni,nj가 시작점과 같다면
                # 처음에 방문표시했던 제자리로 돌아와야 하기때문에 방문조건을 빼고 진행
                ans = 1 # ans를 1로 선언해주면서
                return # 함수를 종료
            if arr[ni][nj] == color and v[ni][nj] == 0: # ni,nj의 색과 color가 같고 방문하지 않았다면
                v[ni][nj] = 1 # 방문표시를 해주고
                dfs(ni,nj,pi,pj,cnt+1,color) # 재귀로 dfs함수 실행
                v[ni][nj] = 0 # 방문표시를 해제

def cycle():
    for i in range(N):
        for j in range(M):
            si, sj = i, j # dfs 함수에서 ni, nj 로 값이 변할 변수
            pi, pj = i, j # dfs 함수에서 ni, nj 와 값을 비교하기 위해 파라미터로 활용
            v[si][sj] = 1 # 방문 표시
            cnt = 1 # dfs의 깊이에 해당하는데, 1로 초기화하고 dfs 함수 내에서 조건문으로 활용하기 위해 파라미터로 활용
            color = arr[i][j] # 보기 편하게 color로 재선언
            dfs(si,sj,pi,pj,cnt,color)
            if ans: # ans가 1이라면 함수를 종료하면서 'Yes'를 리턴
                return 'Yes'
    return 'No' # for문을 다 돌았음에도 이전에 'yes'로 리턴되지 않았다면 싸이클 존재x 이므로 'No'를 리턴

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0 # ans를 0으로 초기화 시켜서 진행

print(cycle()) # cycle 함수 실행