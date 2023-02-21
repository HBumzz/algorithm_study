import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(N):
    v = [0] *(node+1)
    q = deque()
    q.append(1)
    while q:
        t = q.popleft()
        for n in adj[t]:
            if v[n] == 0 :
                v[n] = 1
                q.append(n)
    return v
node = int(input())
link = int(input())
adj = [[] for _ in range(node+1)]
for _ in range(link):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
ans = bfs(1)
print(ans.count(1)-1)