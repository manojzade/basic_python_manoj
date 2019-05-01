def fact(num ):
    if num==0:
        return 1
    else:
      return fact(num-1)*num

print("factorial ofr 5 is  " + str(fact(5)))
for i in range (1,10):
    print(f"factorial of {i} is  " + str(fact(i)))