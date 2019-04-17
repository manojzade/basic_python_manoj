# WAP to swap the value of two variables in Python without using third variable

x,y=6,8
print(f"here  x is : {x} and y is {y}")
y,x=x,y
print(f"now x is : {x} and y is {y}")


# 2) WAP to create a DS of students (define DS as per the protocols)
# and print the sum of scores in five subjects and gets the each student percentage.

dict_student ={"Maths":65,"English":80,"Physics":89,"Chemistry":70,"Hindi":92}
tot=0
for sub,marks in dict_student.items():
    tot=tot+dict_student.get(sub)

percent=tot/(len(dict_student))
print("Total Marks :",tot)
print("Percentage " ,percent)



