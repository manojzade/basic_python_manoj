def reverse_num(num):
    new_num = 0
    while num >0:
        temp = num % 10
        num =num//10

        new_num = int(new_num)*10 + temp
        # print(new_num)
    return  new_num

print(reverse_num(1201000001))
print(reverse_num(987654321))


def reverse_num_RECUR(num):

    if num<10:
        return num
    else:
        # print(str(num%10))
        return  (str(num%10)+str(reverse_num_RECUR(num//10)))


print('see Reverse ',reverse_num_RECUR(410010699900012066))



