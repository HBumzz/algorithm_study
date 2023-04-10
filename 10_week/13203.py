import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(idx,depth):
    if depth == 5:
        return
    v[idx] = 1
    for i in adj[idx]:
        if not v[i]:
            dfs(i,depth+1)
N, M = map(int, input().split())

adj = [[] for _ in range(N)]
v = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
real_ans = 0

for i in range(len(adj)):
    depth = 1
    if adj[i] and v[i] == 0:
        dfs(i,depth)
    print(depth)
    if depth >= 5:
        real_ans = 1
        break
print(v)
print(real_ans)