def check_leap_yr(y):
    if y%400 ==0:
        return True
    elif y%400!=0 and y%100==0:
        return False
    elif y%4 == 0:
        return True
    else :
        return  False

print(check_leap_yr(2020))
