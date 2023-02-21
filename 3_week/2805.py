T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 7일때 1,3,5,7,5,3,1
    ans = 0
    for i in range(N//2+1):
        for j in range(N//2-i,N//2+i+1):
            ans +=arr[i][j]
    for i in range(N//2):
        for j in range(N//2-i,N//2+i+1):
            ans +=arr[-(i+1)][j]
    print(f'#{test_case} {ans}')