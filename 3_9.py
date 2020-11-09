def count_prime(n):
    ctr=0
    for num in range(1,n):

        if num<=1:
            continue

        for i in range(2,num):
            if (num% i == 0):
               break
        else:
            ctr +=1
    return ctr
a=int(input("enter  no:"))
print(count_prime(a))
