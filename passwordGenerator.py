import random
import string

randomChar = string.ascii_letters + string.punctuation + string.digits
passwordLen = int(input("Enter the length of your password :- "))

password = ""
for i in range(passwordLen):
    password += random.choice(randomChar)

print("Your password is :- ",password)