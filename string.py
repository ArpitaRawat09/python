# Palindrome Question

name = "naman"
rev = ""
for i in range(len(name) - 1, -1, -1):
    rev = rev + name[i]
if name == rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")





# name = "ArpitaRawatfromBagdakhurd"
# store = ""
# for i in range(len(name) - 1, -1, -1):
#     store = store + name[i]
# print(store)
#     # print(name[i])
