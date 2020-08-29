a=int(input("enter the starting number of range:"))
b=int(input("enter the last number of range:"))
def test_range(n):
    if n in range(a,b):
        print("in range")
    else:
        print("out of range")
test_range(int(input("enter number:")))

