import sys
sys.stdin = open('input.txt', 'r')

def turn(num,direction):
    if direction == 1:
        arr[num] = arr[num][7:] + arr[num][:7]
    else:
        arr[num].append(arr[num].pop(0))

    return num, direction

arr = [list(map(int, input())) for _ in range(4)]
N = int(input())
move = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    num, direction = move[i]
    num -=1
    temp_num, temp_direction = num, direction
    flag = [0,0,0]
    for j in range(3):
        if arr[j][2] != arr[j+1][6]:
            flag[j] = 1
    turn(num, direction)
    k = 1
    while True: # 왼쪽
        if num-k < 0:
            break
        if flag[num-k] :
            if direction == 1:
                num, direction = turn(num-k, direction-2)
            else:
                num, direction = turn(num-k, direction+2)
        else:
            break
    num, direction = temp_num, temp_direction
    k = 1
    while True: # 오른쪽
        if num + k > 3:
            break
        if flag[num+k-1] :
            if direction == 1:
                num, direction = turn(num+k, direction-2)
            else:
                num, direction = turn(num+k, direction+2)
        else:
            break

ans = 0
for i in range(len(arr)):
    if arr[i][0] == 1:
        ans+=2**i
print(ans)
