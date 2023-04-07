N, M = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

start, end = 1, max(lst)
while (start <= end):
    cnt = 0
    mid = (start+end)//2
    for i in range(N):
        cnt += lst[i]//mid
    if cnt >= M:
        start = mid+1
    else:
        end = mid -1
print(end)