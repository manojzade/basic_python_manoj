# 6)	WAP to find the distinct, duplicate and unique elements in a list.


list =[1,2,3,5,3,1,6,9]
unique=set(list)
# print(unique)
dupli=[]
distinct =[]
for i in list:   #take full list
    count =0
    for j in list:  # check each item repetion
        if i==j:
            count+=1
    if count>1:       # it has duplicate
        if i not in dupli:    #consider onlt o
          dupli.append(i,)



print(dupli)


