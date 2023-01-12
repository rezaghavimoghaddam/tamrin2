
import math

op = input("what you need? (* , / , - , + , sin , cos , tan , cot , radical , factorial) : ")

if op == "*":
    a = float(input("enter a : "))
    b = float(input("enter b : "))

if op == "+":
    a = float(input("enter a : "))
    b = float(input("enter b : "))    

if op == "-":
    a = float(input("enter a : "))
    b = float(input("enter b : "))

if op == "/":
    a = float(input("enter a : "))
    b = float(input("enter b : "))

if op == "sin":
    x = float(input("enter x : "))

if op == "cos":
    x = float(input("enter x : "))

if op ==  "tan":
    x = float(input("enter x : "))

if op ==  "cot":
    x = float(input("enter x : "))

if op == "radical":
    x = float(input("enter x : "))

if op == "factorial":
    x = int(float("enter x : "))    

if op == "*":
    print(a * b) 

if op == "+":
    print(a + b)

if op == "-":
    print(a - b)

if op == "/":
    print(a / b) 

if op == "sin":
    print(math.sin(x))

if op == "cos":
    print(math.cos(x))

if op == "tan":
    print(math.tan(x))

if op == "cot":
    print((math.sin(x) * math.cos(x)))

if op == "factorial":
    print(math.factorial(x))

if op == "radical":
    print(math.sqrt(x) )           
