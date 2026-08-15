# thisset = {"apple", "banana", "cherry", True, 1, 2,8,"arpita" , False,0}

# print(thisset)


# Methods of Sets

fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
fruits.add("apple")

print(fruits)



fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
x.difference_update(y)
z = x.intersection(y)

print(z)
print(x)
print(z)