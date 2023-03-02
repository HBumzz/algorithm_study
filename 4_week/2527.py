import sys
sys.stdin  = open('input.txt','r')
for i in range(4):
    x1,y1,p1,q1, x2,y2,p2,q2 = map(int, input().split())
    mx_x = max(x1,x2)
    mx_y = max(y1,y2)
    mn_p = min(p1,p2)
    mn_q = min(q1,q2)
    x_diff = mn_p-mx_x
    y_diff = mn_q-mx_y
    if x_diff > 0 and y_diff > 0 :
        ans = 'a'
    elif x_diff < 0 or y_diff < 0 :
        ans = 'd'
    elif x_diff ==0 and y_diff == 0 :
        ans = 'c'
    else:
        ans= 'b'
    print(ans)