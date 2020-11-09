def summer_69(lst):
    record=True
    sum=0
    for n in lst:
        if(n==6):
            record=False
        if record:
            sum+=n
        if n==9:
            record=True
    return sum
lst=[]
n=int(input("enter the no. of element:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)


print(summer_69(lst))
