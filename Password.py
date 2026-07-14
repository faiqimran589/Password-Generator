import random
import string
characters=(
    string.ascii_letters+
    string.digits+
    string.punctuation
)
password=""
for i in range(8):
    password=password+random.choice(characters)

print("your password is:",password)