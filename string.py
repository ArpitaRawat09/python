# Count special characters
str = "a123evnu#%1!*najia"

digit = 0
char = 0
schar = 0
for i in str:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        schar += 1

print(f"Digits are = {digit} \nCharacters are = {char} \nSpecial char are = {schar}")


# Palindrome Question

# name = "naman"
# rev = ""
# for i in range(len(name) - 1, -1, -1):
#     rev = rev + name[i]
# if name == rev:
#     print("String is Palindrome")
# else:
#     print("String is not Palindrome")


# name = "ArpitaRawatfromBagdakhurd"
# store = ""
# for i in range(len(name) - 1, -1, -1):
#     store = store + name[i]
# print(store)
#     # print(name[i])
