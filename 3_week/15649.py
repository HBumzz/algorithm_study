N, M = map(int , input().split())

lst = []
def dfs():
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1,1+N):
            if i not in lst:
                lst.append(i)
                dfs()
                lst.pop()
dfs()