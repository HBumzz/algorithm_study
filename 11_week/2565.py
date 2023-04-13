N = int(input())
lst = [0]*N
for i in range(0,N):
    a, b = map(int, input().split())
    lst[i] = [a,b]
lst.sort()
dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(lst)
print(dp)
print(N-max(dp))