def dfs(depth, sm,plus, minus, mul, div):
    global mx, mn
    if depth == N:
        if sm > mx:
            mx = sm
        if sm < mn:
            mn = sm
        return
    if plus:
        dfs(depth+1, sm+lst[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, sm-lst[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, sm*lst[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(sm/lst[depth]), plus, minus, mul, div-1)

N = int(input())
lst = list(map(int, input().split()))
cal = list(map(int, input().split()))
mn = 1e9
mx = -1e9
dfs(1,lst[0],cal[0],cal[1],cal[2],cal[3])
print(mx)
print(mn)