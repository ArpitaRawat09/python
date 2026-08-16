# Zero Division errror :- Exceptions

a = int(input("enter number :- "))

# b = (10/a)
# print(b)


try:
    print(10 / a)
except ZeroDivisionError:
    print("Sorry you can't divide by 0")
    

print("ok i have done by zero")


# syntax error

# x = [1,2,3,4,5]

# for i in x:
# print(i)


# indentation error
# for i in x
#     print(i)
