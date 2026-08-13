# Palindrome Question

name = "nama"
rev = ""
cpy = name
for i in range(len(name) - 1, -1, -1):
    rev = rev + name[i]
if cpy == rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")





# name = "ArpitaRawatfromBagdakhurd"
# store = ""
# for i in range(len(name) - 1, -1, -1):
#     store = store + name[i]
# print(store)
#     # print(name[i])
