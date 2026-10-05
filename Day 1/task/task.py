# name = input("What is your name?")
# print(name)
#
# print(len(name))

# username = input("What's your name?")
# length = len(username)
# print(length)

# Variables challenge
glass1 = "milk"
glass2 = "juice"

# Before
print("The content of the first glass is: " + glass1)
print("The content of the second glass is:" + glass2)

# After altering the content

temp = glass1
glass1 = glass2
glass2 = temp

print("==========================")
print(glass1)
print(glass2)