def almost_there(n):
    if(abs(200-n)<10 or abs(100-n)<10):
        return True
    else:
        return False
n=int(input("enter the no.:"))
print(almost_there(n))
