import sys
sys.setrecursionlimit(10*4)
def dfs(idx,depth):
    global flag
    if depth == 5:
        flag = 1
        return
    v[idx] = 1
    for i in adj[idx]:
        if not v[i]:
            v[i] = 1
            dfs(i,depth+1)
            v[i] = 0
N, M = map(int, input().split())

adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
flag = 0
real_ans = 0
for i in range(len(adj)):
    v = [0] * N
    depth = 1
    if adj[i] and v[i] == 0:
        dfs(i,depth)
    if flag:
        real_ans = 1
        break
print(real_ans)