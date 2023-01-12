name = input("type your name: ")
family = input("type your family: ")
math_s = float(input("type your math score: "))
li_s = float(input("type your literature score: "))
lang_s = float(input("type your laguage score: "))

average = (math_s + li_s + lang_s) / 3 

print(name, family, average)

if average >= 17:
    print("great")

if average >= 12 and average < 17:
    print("normal")

if average < 12:
    print("fail")
