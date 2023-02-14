# 자기 기준으로 오른쪽으로 벽찍고 왼쪽으로 벽찍고 무한반복
# 자기기준으로 위로 벽찍고 아래로 벽찍고 무한반복
import sys
sys.stdin = open('input.txt', 'r')
w, h = map(int, input().split())
x, y = map(int, input().split())
sec = int(input())
x_mok, y_mok = (x+sec)//w, (y+sec)//h
if x_mok%2 == 1:
    ans_x = w - (x+sec)%w
else:
    ans_x = (x+sec)%w
if y_mok%2 == 1:
    ans_y = h- (y+sec)%h
else:
    ans_y = (y+sec)%h
print(ans_x,ans_y)