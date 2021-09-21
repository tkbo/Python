import math
a = float(input("podaj a"))
b = float(input("podaj b"))
c = float(input("podaj c"))


delta = (b**2)-(4*a*c)
print(delta)

if delta>0:
    x1 = ((-b)+(math.sqrt(delta)))/(a*2)
    x2 = ((-b)-(math.sqrt(delta)))/(a*2)
    mniejniz0x1 = f"x1= {x1}"
    print(mniejniz0x1)
    mniejniz0x2 = f"x2= {x2}"
    print(mniejniz0x2)
else:
    if delta==0:
        x = (-b)/(2*a)
        rowne0x = f"x= {x}"
        print(rowne0x)
    else:
     if delta<0:
        print("Nie ma rozwiązań")


