a = int(input("Enter first :"))
b = int(input("Enter second :"))
c = int(input("Enter third :"))

if(a>=b):
    if(a>=c):
        print("Greatest numer is", a)
    else:
        print("Greatest numer is", c)
elif(b>=a):
    if(b>=c):
        print("Greatest numer is", b)
    else:
        print("Greatest numer is", c)    
    
        