# Basic Examples for practice

for i in range(1, 21):
    print(i)


# Reverse loop
for i in range(20, 0, -1):
    print(i)


# table
num = 2
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")

n = int(input("which table you want to print :- "))
for i in range(n, n * 10 + 1, n):
    # print(f"{n} * {i} = {n*i}")
    print(i)
