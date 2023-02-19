import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    mx = 0
    for i in range(N):
        for j in range(i+1,N):
            result = lst[i]*lst[j]
            str_result = str(result)
            if len(str_result) == 1: # 한자리 수 인거 처리
                continue
            for k in range(1,len(str_result)):
                if int(str_result[k]) < int(str_result[k-1]):
                    break
            else:
                if result > mx:
                    mx = result
    if mx == 0: # mx가 갱신이 안되었다는 거는 단조증가수가 없다는 뜻
        ans = -1
    else:
        ans = mx
    print(f'#{test_case} {ans}')
    