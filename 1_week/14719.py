# 가장 큰수 찾기, 양쪽으로 자기보다 같거나 작은 수 찾고
# 그 찾은 블럭의 크기에서 그 사이 인덱스 블럭들 차이를 다더함 걍 무한 반복
# 첨에 가장 큰수가 0 이다 -> 0 or 블럭이 한줄이다 == 두번째max가 0이다 -> 0
import sys
sys.stdin = open('input.txt', 'r')
H, W = map(int, input().split())
lst = list(map(int, input().split()))
mx = max(lst)
if mx == 0 or sorted(lst)[-2] == 0:
    print(0)
else:
    cnt = 0
    present_idx = lst.index(mx)
    while True: # 왼쪽 탐색부터 max값을 계속 바꿔주고, 그 이전 맥스값을 저장해둬야댐
        # mx 인덱스가 0이랑 끝점이면 어케 고려할건가
        # idx 가아닌
        past_idx = present_idx
        if len(lst[past_idx-1::-1]) == 0:
            break
        else :
            mx = max(lst[past_idx-1::-1])
        if past_idx <= 0 or mx ==0 : # 여기 다시한번 생각해보자
            break
        diff = lst[past_idx-1::-1].index(mx) # max를 사용하려면 슬라이싱을 어떻게 할지 생각해야댐
        present_idx = past_idx-(diff+1)
        if present_idx - past_idx == 1:
            continue
        else:
            for i in lst[past_idx-1:present_idx:-1]:
                cnt += mx-i
    present_idx = lst.index(mx)
    while True: # 오른쪽으로 탐색
        past_idx = present_idx
        if len(lst[past_idx+1::]) == 0:
            break
        else:
            mx = max(lst[past_idx+1::])
        if past_idx >= W-1 or mx == 0:
            break
        diff = lst[past_idx+1::].index(mx)
        present_idx = past_idx+diff+1
        if present_idx - past_idx == 1:
            continue
        else:
            for i in lst[past_idx+1:present_idx:]:
                cnt+= mx-i
    print(cnt)