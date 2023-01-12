a = float(input("enter a : "))
b = float(input("enter b : "))
c = float(input("enter c : "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("yes")
else:
    print("no")
