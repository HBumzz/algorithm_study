N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0] # 49 선택후 같은 열이 아닌 열중에 직전 행에서 작은값 40을 더함 89
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1] # 60 선택후 26을 더함 86
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2] # 57 선택후 26을 더함 83
    for i in range(3):
        print(arr[i])
    print('----------')
print(min(arr[N-1][0], arr[N-1][1], arr[N-1][2]))