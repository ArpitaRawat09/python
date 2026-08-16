# Find the frequency

x = [1, 1, 2, 3, 2, 4, 3, 5, 9, 9, 9, 2, 4, 1, 1, 0]
d = {}
freq = 0
for i in x:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1    

print(d)


# dictonary = {"name": "Arpita", "age ": 22, "degree": "MCA", "clg": "SVVV"}
# print(dictonary)
# print(dictonary["name"])

# for i in dictonary:
#     print(dictonary[i])

# dictonary.update({"city":"Indore"})
# x = dictonary.values()
# print(x)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model", "Bronco")

# print(x)
# print(car)
