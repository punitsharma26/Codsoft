import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "!@#$%^&*()_+-=<>?,./?:"

allChar = letters + num + symbols

n = int(input("Enter length of password: "))
password = ""
for _ in range(n):
    password += random.choice (allChar)

print(f"Your password of {n} character is: {password}")



# Using OOPs

class PasswordGen:
    def __init__(self):
        self.length = 0
        self.char= allChar
    def input_var(self):
        self.length = int(input("Enter length of password: "))
    def generate(self):
        self.password = ""
        for _ in range(self.length):
            self.password += random.choice (allChar)
        return self.password

obj=PasswordGen()
obj.input_var()
print(obj.generate())
