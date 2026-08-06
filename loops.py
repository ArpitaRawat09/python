# Basic Examples for Loops practice

# Login System

correct_name = "admin"
correct_password = 1234

for i in range(3):
    name = input("Enter Username: ")
    password = int(input("Enter Password: "))

    if name == correct_name and password == correct_password:
        print("✅ Login Successful")
        break
    else:
        print("❌ Invalid Username or Password")

else:
    print("🔒 Account Locked")


# for i in range(1, 21):
#     print(i)


# # Reverse loop
# for i in range(20, 0, -1):
#     print(i)


# # table
# num = 2
# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")

# n = int(input("which table you want to print :- "))
# for i in range(n, n * 10 + 1, n):
#     # print(f"{n} * {i} = {n*i}")
#     print(i)

# Looops for String

# a = "I am a full stack web Developer"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


# use of break
# for i in range(1, 21):
#     if i == 12:
#         break
#     print(i)

# print even number

# for i in range(1, 21):
#     if i % 2 == 1:
#         print(f"Odd number is: {i}")
#         break

# else:
#     print(f"{i} is not a even number")
