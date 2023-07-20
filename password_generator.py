
import random
passlength = int(input("enter the length of password:"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(s,passlength ))
print("password:",password)