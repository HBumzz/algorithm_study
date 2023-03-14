import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append([i,j])
        elif arr[i][j] == 1:
            homes.append([i,j])
ans = 5000
for combination in combinations(chickens, M):
    sm = 0
    for i in range(len(homes)):
        dist = 100
        hi, hj = homes[i]
        for j in range(M):
            ci, cj = combination[j]
            dist_ = abs(hi-ci) + abs(hj-cj)
            if dist_ < dist :
                dist = dist_
        sm += dist
    if sm < ans :
        ans = sm
print(ans)