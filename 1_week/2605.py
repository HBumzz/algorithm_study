N = int(input())
num = list(map(int,input().split()))
lst = []
for i in range(N):
    lst.insert(num[i], i+1)
lst.reverse()
print(*lst)