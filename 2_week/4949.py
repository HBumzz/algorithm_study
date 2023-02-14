import sys
sys.stdin = open('input.txt', 'r')
while True:
    Str = input()
    lst = []
    if Str == '.':
        break
    for s in Str:
        if s == '(':
            lst.append(s)
        elif s == ')':
            if lst and lst[-1] == '(':
                lst.pop()
            else:
                lst.append(s)
                break
        elif s == '[':
            lst.append(s)
        elif s ==']':
            if lst and lst[-1] == '[':
                lst.pop()
            else:
                lst.append(s)
                break
    if len(lst) == 0:
        result = 'yes'
    else:
        result = 'no'
    print(result)