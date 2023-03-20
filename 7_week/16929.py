# def dfs(arr):
#
#

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
st = set()
for i in range(N):
    for j in range(M):
        st.add(arr[i][j])
lst = list(st)
