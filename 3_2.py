def lesser_of_two_evens(n1,n2):
    if((n1%2==0) and (n2%2==0)):
        if(n1>n2):
            return n2
        else:
            return n1
    else:
        if(n1>n2):
            return n2
        else:
            return n1
a=int(input("enter first no. :"))
b=int(input("enter second no. :"))
print(lesser_of_two_evens(a,b))
