string=input("enter the string:")
low=0
up=0
for i in string:
    if i.isupper():
        up+=1
    if i.islower():
        low+=1
print("uppercase letter :",up)
print("lowercase letter:",low)


