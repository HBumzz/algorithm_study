import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(n):
    v = [-1]*(N+1)
    v[n] += 1
    q = deque()
    q.append(n)
    while q:
        t = q.popleft()
        for i in adj[t]:
            if v[i] == -1:
                v[i] = v[t] + 1
                q.append(i)
    return max(v)

N = int(input())
adj = [[] for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)
score = 50
lst = []
for n in range(1, N+1):
    tmp = bfs(n)
    if tmp < score:
        score = tmp
        lst = [n]
    elif tmp == score:
        lst.append(n)
print(score, len(lst))
print(*lst)
