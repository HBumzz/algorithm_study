R, C, M = map(int, input().split())
sharks = dict()

for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    sharks[(r-1,c-1)] = [s,d,z]
fisherman = -1
res = 0
for _ in range(C):
    fisherman +=1
    for  i in range(R):
        if (i, fisherman) in sharks:
            shark = sharks[(i,fisherman)]
            res += shark[2]
            del shark
    next_sharks = dict()
    for key, value in sharks.items():
        x, y = key
        s,d,z = value
        if d==1 or d==2:
            s = s % (R*2-2)
        else:
            s = s % (C*2-2)
        while s:
            if d==4:
                if y>s:
                    y-=s
                    s=0
                else:
                    y=0
                    s-=y
                    d=3
            elif d==3:
                if C-y-1 > s:
                    y += s
                else:
                    s -= (C-y-1)
                    y = C-1
                    d = 4
    if (x, y) in next_sharks:
        if z > next_sharks:
            next_sharks[(x,y)] =[s,d,z]
    else:
        next_sharks[(x,y)] = [s,d,z]
    sharks = next_sharks
