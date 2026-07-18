import random
import string
l=int(input('Length of your password is:'))
characters=(
    string.ascii_letters+
    string.digits+
    string.punctuation
)

password=""
for i in range(l):
    password=password+random.choice(characters)

print("your password is:",password)