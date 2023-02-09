# 1은 북, 2 남, 3 서, 4 동 왼쪽경계로부터의 거리
# 그냥 시계로 돌고 반시계로돌고 작은거 뽑아서 sum으로 출력하면 될듯?
import sys
sys.stdin = open('input.txt', 'r')
length, height = map(int, input().split())
T = int(input())
arr = [[0]*(length+1) for _ in range(height+1)]
dic_guard = {1:0, 2:height, 3:0, 4:length} #1일때 i=0, 2일때 i는 height-1, 3일때 j는 0, 4일때 j는 length-1

# 경비원의 좌표
sec_lst = []
for _ in range(T):
    a,b = map(int, input().split())
    if a == 1 or a == 2:
        i, j = dic_guard[a], b
    else:
        arr[b][dic_guard[a]] += 1
        i, j = b, dic_guard[a]
    sec_lst.append([i,j])
# 나의 좌표를 x,y로 다시 선언
x, y = map(int , input().split())
if x == 1 or x == 2:
    x, y = dic_guard[x], y
else:
    x, y = y, dic_guard[x]
## 북북, 남남, 서서, 동동, /북남 , 서동 /북동 북서
# print(sec_lst)
# print(x,y)
result = 0
# print(abs(sec_lst[0][0]-x))
# print(height)
# print(height)
# print(y)
# print(sec_lst[0][1])
# print(sec_lst)
for tc in range(T):
    if x == sec_lst[tc][0]:
        ans = abs(sec_lst[tc][1]-y)
        # print(0)
    elif y == sec_lst[tc][1]:
        ans = abs(sec_lst[tc][0]-x)
        # print(1)
    # 반대편에 있을때
    elif abs(sec_lst[tc][0]-x) == height :
        if x+sec_lst[tc][0] <= (height-x)+(height-sec_lst[tc][0]):
            ans = height + y + sec_lst[tc][1]
            # print(2)
            # print(f'tc0 {ans}')
        else:
            ans = height + length-y + length-sec_lst[tc][1]
            # print(3)
    elif abs(sec_lst[tc][1]-y) == length:
        if y + sec_lst[tc][1] <= (length - y) + (length - sec_lst[tc][1]):
            ans = length + x + sec_lst[tc][0]
            # print(4)
        else:
            ans = length + height - x + height-sec_lst[tc][0]
            # print(5)
    else: # 옆 위 or 옆 아래
        ans = abs(sec_lst[tc][0]-x) + abs(sec_lst[tc][1]-y)
        # print(6)
    result += ans
    # print(f'ans {ans}')
print(result)
# 5 5 0 나오는데 -> 2 5 0 나와야댐
# 12 6 5 나와야되는데 10 6  나옴