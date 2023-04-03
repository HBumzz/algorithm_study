def promising(x):
    for i in range(x):
        if v[x] == v[i] or abs(v[x]-v[i]) == abs(x-i):
            return 0
    return 1 # i,j에 퀸을 놓을 수 있음

def f(x):
    global cnt
    if x == N:
        cnt +=1
        return
    else:
        for i in range(N):
            v[x] = i
            if promising(x): # promising 다돌아서 놓아진 상태
                f(x+1)
N = int(input())
v = [0] *N
cnt = 0
f(0)
print(cnt)