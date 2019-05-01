def get_prime(num):
    for i in range(2,num+1):
        k=0
        for j in range(2,i//2+1):
            if i%j==0:
               k+=1
        if k<=0:
                print(i)


get_prime(99)