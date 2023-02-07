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
for i in range(1,N): # 2 6 10 # 1 4 9 16
    k = i*(i+1)
    s = i*i
    lst_k.append(k)
    lst_s.append(s)
idx_lst = [0]*N**2
for idx in lst_k:
    idx_lst[idx] += 1
for idx in lst_s:
    idx_lst[idx] += 1

dx = [-1,0,1,0] # 위 오른쪽 아래 왼쪽
dy = [0,1,0,-1]
arr = [[0]*N for _ in range(N)]
x, y = int(N//2), int(N//2)
arr[x][y] = 1
k = 0
j = 2
for i in range(1, len(idx_lst)):
    arr[x+dx[k%4]][y+dy[k%4]] = j
    j+=1
    x, y = x+dx[k%4], y+dy[k%4]
    if idx_lst[i] == 1:
        k+=1
for i in range(N):
    print(*arr[i])
for i in range(N):
    for j in range(N):
        if num == arr[i][j]:
            print(i+1, j+1)
