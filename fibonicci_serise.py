def fibb_series(range):
    if range==0:
        return  1
    elif range==1:
        return 1
    else:
        return fibb_series(range-1)+fibb_series(range-2)
#####print fibonici series
for i in range (0,8):
    print(f"for {i} : " +   str(fibb_series(i)))


def lucas_num(num):
    if num==0:
        return 2
    elif num==1:
        return 1
    else:
        return lucas_num(num-1) +lucas_num(num-2)
#print lucas  series
for i in range (0,8):
    print(f"for {i} : " +   str(lucas_num(i)))
