# 6)	WAP to find the distinct, duplicate and unique elements in a list.


list =[1,2,3,5,3,1,6,9]
unique=[]
dupli=[]
distinct =[]
for i in list:
    if  ( not i in  distinct):
       distinct.append(i)

print(distinct)


