

def cal_gross_sal (basic, DA,TA):
    return basic+(basic*DA/100)+ (basic*TA/100)

base= int(input("Enter Basic sal :  "))

print("For basic of {base} : is Gross is ",cal_gross_sal(base,10,12)  )