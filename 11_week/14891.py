def moving(direction, num):
    if direction == 1:
        right = arr[num][2] # 오른쪽 접면
        left = arr[num][6]  # 왼쪽 접면
        for _ in range(7):
            arr[num].append(arr[num].pop(0)) #방향전환
    else:
        right = arr[num][2]  # 오른쪽 접면
        left = arr[num][6]
        arr[num].append(arr[num].pop(0)) # 방향전환
    return direction, left, right

arr = [list(map(int, input())) for _ in range(4)]
N = int(input())
move = [list(map(int, input().split())) for _ in range(N)]
for i in range(len(move)):
    num, direction =move[i]
    num -= 1 # 하나빼줌
    direction, left, right = moving(direction,num)
    k = 1
    while True: # 왼쪽
        if num-k < 0:
            break
        if left != arr[num-k][2]:
            if direction == 1:
                direction = -1
            else:
                direction = 1
            moving(direction,num-k)
        k+=1
    k = 1
    while True:
        if num+k > 3:
            break
        if right != arr[num+k][6]:
            if direction == 1:
                direction = -1
            else:
                direction = 1
            moving(direction,num+k)
        k+=1
print(arr)
ans = 0
for i in range(4):
    print(arr[i][0])
    if arr[i][0] == 1:
        ans += 2**i
print(ans)