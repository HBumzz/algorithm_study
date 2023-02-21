import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    mx = 0
    for i in range(N):
        for j in range(i+1,N): # i < j
            result = lst[i]*lst[j]
            str_result = str(result) # 한자리수 처리하기 위해
            if len(str_result) == 1: # 한자리 수 인거 처리
                continue
            for k in range(1,len(str_result)):
                if int(str_result[k]) < int(str_result[k-1]):
                    break
            else: # 단조 증가하는 수라면
                if result > mx:
                    mx = result # 최대값 갱신
    if mx == 0: # mx가 갱신이 안되었다는 의미는 단조 증가하는 수 가 없다는 뜻
        ans = -1
    else:
        ans = mx
    print(f'#{test_case} {ans}')
    