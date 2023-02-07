N = int(input())
num = int(input())
# dx,dy의 index 0 1/ 2 2 3 3 / 0 0 0 1 1 1 ~~
# 2 4 6 8 개씩 증가 -> 어케구현할래? ㅜ
#i[1,2  3,4,5,6  7,8,9,10,11,12]
# [0,1, 2,2,3,3, 4,4,4,5,5,5  6,6,6,6,7,7,7,7]
# [1,2 1,2,3,4, 1,2,3,4,5,6]
# j 는 c로 나누었을때 나누어 떨어지면 j+1
lst_k = []
lst_s = []
for i in range(1,N+1): # 2 6 10 # 1 4 9 16
    k = i*(i+1)
    s = i*i
    lst_k.append(k)
    lst_s.append(s)
lst_value = []
value = -2
for i in range(1,N*N+1):
    if i in lst_s:
        value +=1
    elif i in lst_k:
        value +=1
    else:
        lst_value.append(value)
real_value = []
for i in lst_value:
    i = i%4
    real_value.append(i)
arr = [[0]*N for _ in range(N)]
x, y = int(N//2), int(N//2)
arr[x][y] = 1
dx = [-1,0,1,0] # 위 오른쪽 아래 왼쪽
dy = [0,1,0,-1]
snail = 2
for i in range(N*N-1):
    arr[x+dx[real_value[i]]][y+dy[real_value[i]]] = snail
    snail +=1
    x,y = x+dx[real_value[i]], y+dy[real_value[i]]
for i in range(N):
    print(arr[i])
for i in range(N):
    for j in range(N):
        if arr[i][j] == num:
            print(i+1,j+1)