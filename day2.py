#find maximum of 2 numbers.

#using if-else
# def findMax(n1,n2):
#     if n1>n2:
#         print(n1,'is greater than ',n2)
#     elif n1<n2:
#         print(n2,'is greater than ',n1)
#     else:
#         print('both are equal')
# a=int(input('enter first number:'))
# b=int(input('enter secong number:'))
# findMax(a,b)

#using lambda function
# findMax=lambda a,b:print(a ,'is greater than ',b) if a>=b else print(b ,'is greater than ',a)
# findMax(23,45)
#using max()

a=int(input('enter first number:'))
b=int(input('enter secong number:'))
# print(max(a,b))

#using ternary operator
# print(a if a>b else b)
#using list comprehension
# l=[a if a>b else b]
# print(l)

#using sort()
x=[a,b]
x.sort()
print(x)
print(x[-1])


    