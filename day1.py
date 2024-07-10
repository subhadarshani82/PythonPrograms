#adding 2 numbers 
#*********************************************
#using + operator
# a= int(input('enter forst number:'))
# b= int(input('enter second number:'))
# c=a+b
# print(c)
#**************************************************
#by defining a function
# def addition(a,b):
#     c=a+b
#     print(c)
# addition(3,7)
# **************************************************************
# by using operator.add method

# import operator
# sum=operator.add(a,b)
# print(sum)

#****************************************************
#by using lambda function
# sum=lambda a,b:a+b
# print(sum(23,45))

#by recursive function
def add(a,b):
   if b==0:
       return a
   else:
       return add(a+1,b-1)
result=add(23,45)
print(result)