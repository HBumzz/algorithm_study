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
# 둘레
size = 2*(length+height)
ans = 0
for tc in range(T):
    len_lst = []
    if x == sec_lst[tc][0] and (x==0 or x== height):
        ans += abs(sec_lst[tc][1]- y)
    elif y == sec_lst[tc][1] and (y==0 or y== length):
        ans += abs(sec_lst[tc][0]-x)
    else: #(0,0) (height,0) (height, len) (0 len)
        # 각 꼭지점과의 거리를 다구하고 가장 짧은거 구함
        len_lst.append(x + y + sec_lst[tc][0] + sec_lst[tc][1])
        len_lst.append(2*height-x + y - sec_lst[tc][0] + sec_lst[tc][1])
        len_lst.append(2*length+x - y + sec_lst[tc][0] - sec_lst[tc][1])
        len_lst.append(2*(height+length)-x - y - sec_lst[tc][0] - sec_lst[tc][1])
        ans += min(len_lst)
print(ans)