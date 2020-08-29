def printFibonacciNumbers(N):
    n1=0
    n2=1
    if(N<1):
        return
    for i in range(0,N):
        print(n2)
        n3=n1+n2
        n1=n2
        n2=n3
printFibonacciNumbers(int(input("enter limit:")))    
