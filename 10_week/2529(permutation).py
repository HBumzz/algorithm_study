from itertools import permutations

def is_right(permutation):
    for i in range(len(sign_lst)):
        cal =  str(permutation[i]) + sign_lst[i] + str(permutation[i+1])
        if cal[1] == '>':
            if int(cal[0]) < int(cal[2]):
                return False
        else:
            if int(cal[0]) > int(cal[2]):
                return False
    return permutation

N = int(input())
sign_lst = list(map(str, input().split()))
lst_sort = [0,1,2,3,4,5,6,7,8,9]
lst_sort_reverse = [9,8,7,6,5,4,3,2,1,0]

for permutation in permutations(lst_sort_reverse,N+1):
    ans = is_right(permutation)
    if ans:
        print(''.join(map(str,ans)))
        break

for permutation in permutations(lst_sort,N+1):
    ans = is_right(permutation)
    if ans:
        print(''.join(map(str,ans)))
        break

