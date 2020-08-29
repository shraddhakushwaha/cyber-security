list=[1,3,9,9,8,8,6,4,3]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)
print(unique_list)      
