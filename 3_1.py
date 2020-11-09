import string
a=string.ascii_lowercase
def ispangram(str,a):
    aset=set(a)
    return aset<= set(str.lower())
str=input("enter the string:")
print(ispangram(str,a))
