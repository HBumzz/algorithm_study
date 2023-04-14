def moving(num):
    global left, right, direction
    if direction == 1:
        for _ in range(7):
            p = arr[num].pop(0)
            arr[num].append(p) #방향전환
    else:
        arr[num].append(arr[num].pop(0)) # 방향전환
arr = [list(map(int, input())) for _ in range(4)]
N = int(input())
move = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    num, direction = move[i]
    temp = []
    left = arr[num][6]
    right = arr[num][2]
    temp.append([num,direction,left,right])
    moving(num,left,right)
    k = 1
    while True:
        if num-k < 0:
            break
        if left != arr[num-k][2]:
            if direction == 1:
                direction = -1
            else:
                direction = 1
            moving(num-k,arr[num-k][6],arr[num-k][2])
        else:
            break
        k +=1
    k = 1
    num, direction,left,right = temp[0][0], temp[0][1],temp[0][2],temp[0][3]
    while True:
        if num+k > 3:
            break
        if right != arr[num+k][6]:
            if direction == 1:
                direction = -1
            else:
                direction = 1
            moving(num+k,arr[num+k][6],arr[num+k][2])
        else:
            break
        k+=1
print(arr)
ans = 0
for i in range(4):
    value = arr[i][0]
    if value:
        ans += 2**i
print(ans)