def has_33(list1):
    if 3 in list1:
        i = list1.index(3)
        if (list1[i + 1] == 3):
            return True
        else:
            return False
    else:
        return True

lst=[]
n=int(input("enter the no. of element:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

print(has_33(lst))    
