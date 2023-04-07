
N, M, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dir = [[0,1],[0,-1],[-1,0],[1,0]]
# 동서북남
dice = [0,0,0,0,0,0,0]
# 아래 남쪽 서쪽 동쪽 북쪽 반대
#  6
#4 2 3
#  1
#  5

def run(dice, direction):
    if arr[ni][nj] != 0 :
        if direction == 0: # 북쪽
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
            dice[1] = value
            arr[ci][cj] = 0
        elif direction == 1: # 남쪽
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
            dice[1] = value
            arr[ci][cj] = 0

        elif direction == 2: # 서쪽
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
            dice[1] = value
            arr[ci][cj] = 0

        else:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
            dice[1] = value
            arr[ci][cj] = 0

    else:
        if direction == 0: # 북쪽
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
            arr[ci][cj] = dice[1]
        elif direction == 1: # 남쪽
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
            arr[ci][cj] = dice[1]

        elif direction == 2: # 서쪽
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
            arr[ci][cj] = dice[1]
        else:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
            arr[ci][cj] = dice[1]
ci, cj = x, y
for direction in order:
    direction -= 1
    di, dj = dir[direction][0], dir[direction][1]
    ni, nj = ci+di, cj +dj
    if 0<= ni < N and 0<= nj < M :
        value = arr[ni][nj]
        ci, cj = ni, nj
        run(dice, direction)
        print(dice[6])
