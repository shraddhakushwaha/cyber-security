
def spy_game(list1):
    if 700 in list1:
        i = list1.index(0)
        j = list1.index(0)
        k = list1.index(7)
        if (k>j and k>i):
            return True
        else:
            return False
    else:
        return False

lst=[]
n=int(input("enter the no. of element:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

print(spy_game(lst))
