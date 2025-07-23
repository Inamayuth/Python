import random
import string


print("Random Password generator")

print("________________________________")

print()

length=int(input("Enter the length of password = "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

all = lower+upper+number+symbol

temp = random.sample(all,length)
password = " ".join(temp)

print()
print("Your Password is : ",password)
print("________________________________")
