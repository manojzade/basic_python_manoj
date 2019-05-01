def get_greatest_nmuber(a,b,c):
    if a>b and a>c :
        print(str(a) +  "  is gretest ")
    elif b>a and b>c :
        print(str(b) + "  is gretest ")
    else:
        print(str(c) +"  is gretest")


a= input('Enter Ist input')

b= input('Enter 2nd input')

c= input('Enter 3rd input')
print(get_greatest_nmuber(a,b,c))