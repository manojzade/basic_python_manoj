# 12)	WAP to get the count of words in the statement string and the count of vowels in complete statement.
def chec_vowles(ch):
    if ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
        return True

def show_vowels(text):
    a=len(text)
    count =0
    for c in text:
        if chec_vowles(c):
            count+=1
    print("total chars :  " +str(a)  +'  and count of vowels is   ' +  str  (count))

show_vowels('appaeI')
