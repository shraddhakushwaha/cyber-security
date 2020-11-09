def blackjack(a,b,c):
    s=a+b+c
    if( s <=21):
        return s
    else:
        if(((a==11) or (b==11) )or (c==11)):
            if(s-10>21):
                return 'bust'
            else:
                return s-10
        else:
                return 'BUST'
a=int(input("first no:"))
b=int(input("second no:"))
c=int(input("third no:"))
print(blackjack(a,b,c))
