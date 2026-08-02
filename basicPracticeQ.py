# Practice Question

fahrenheit = float(input("Enter temperature in fahrenheit :- "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"Temperature: {celsius:.1f}°C")

if celsius < 0:
    print("Freezing 🥶")
elif 0 <= celsius < 10:
    print("Very Cold 🧥")
elif 10 <= celsius < 20:
    print("Cold ❄️")
elif 20 <= celsius < 30:
    print("Pleasant 😊")
elif 30 <= celsius < 40:
    print("Hot ☀️")
else:
    print("Very Hot 🔥")


# Answer True or False

# Assignment Questions

# print(126 < 120)
# print((456 == 456) != (235 == 236))
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# print(True and bool(0))


# Conditional Statements Questions

# a = 13
# if a>10:
#     print("I will do task A...")
# else:
#     print("I will do task B...")


# a = 5
# if a > 18 and a < 40:
#     print("You are Adult")
# elif a < 18:
#     print("You are minor")
# else:
#     print("You are older")


# Assignment 3
# Question 1

# num1 = int(input("Enter first number :- "))
# num2 = int(input("Enter second number :- "))

# if num1>num2:
#     print("num1 is greater than num2")
# else:
#     print("num2 is greater than num1")

# Question 2

# gender = str(input("Enter the Gender :- "))
# if gender == "female":
#     print("Good Morning Mam.....")
# else:
#     print("Good Morning Sir.....")
