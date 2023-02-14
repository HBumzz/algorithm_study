# 괄호 안에는 뒤집기x, 띄어쓰기 있으면 그 전까지 뒤집기, 나머진 다뒤집기
# < 나오면 > 나올때까지 담는다. ' ' 나오기전까지 또 따로담기
Str = input()
status_lst = []
status = 'reverse'
for i in range(len(Str)):
    if i == len(Str)-1:
        status = 'real_end'
    elif Str[i] == '<':
        status = 'normal'
    elif Str[i] == '>':
        status = 'normal_end'
    elif Str[i] == ' ':
        if status == 'normal':
            pass
        elif status == 'reverse':
            status ='end'
    else:
        if status == 'normal':
            pass
        else:
            status = 'reverse'
    status_lst.append(status)
temp = ''
for i in range(len(Str)):
    if status_lst[i] == 'reverse':
        temp += Str[i]
    elif status_lst[i] == 'real_end':
        temp += Str[i]
        print(temp[::-1], end ='')
    elif status_lst[i] == 'end':
        print(temp[::-1], end=' ')
        temp = ''
    elif status_lst[i] == 'normal' or status_lst[i] == 'normal_end':
        print(temp[::-1], end = '')
        print(Str[i], end = '')
        temp = ''