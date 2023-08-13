import string
import random
len= int(input("enter the length of the password:"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbols=string.punctuation
str=lower+upper+digit+symbols
pwd=random.sample(str,len)
password=" ".join(pwd)
print(password)
