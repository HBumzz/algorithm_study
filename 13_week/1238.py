import sys
sys.stdin = open('input.txt', 'r')

N, M, X = map(int, input().split())
adj = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,time = map(int, input().split())
    adj[a].append((b,time))
print(adj)
start, end = 
dajkstra(start,end)