import sys
n,p = map(int,sys.stdin.readline().split())
my_set = set()
set_len = len(my_set)
v = n
ff = 'T'
my_cnt = 0

while 1 :
    my_set.add(v)
    if set_len == len(my_set) :
        if ff == 'T' :
            my_cnt = 1
            first_value = v
            last_value = -1
            ff = 'F'
        elif first_value == last_value :
            print(my_cnt-1)
            break
        else :
            last_value = v
            my_cnt +=1
    else :
        ff = 'T'

    v = (v*n) % p
    set_len = len(my_set)