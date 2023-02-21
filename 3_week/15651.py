N, M = map(int , input().split())

lst = []
d_lst = []
idx = 0
def dfs():
    global idx
    if len(lst) == M:
        print(' '.join(map(str,lst)))
        return
    else:
        for i in range(1+idx,1+N):
                lst.append(i)
                dfs()
                idx = lst.pop()
dfs()