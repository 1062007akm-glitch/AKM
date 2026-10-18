x = float(input("Enter your first digit :"))
y = float(input("Enter your second digit :"))
choice = int(input("What do you want to calculate(1 for +,2 for -,3 for *,4 for /) :"))

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return"invalid number"
    return a / b
if choice == 1:
    print(x,"+",y,"=",add(x,y))
elif choice == 2:
    print(x,"-",y,"=",sub(x,y))
elif choice == 3:
    print(x,"*",y,"=",mul(x,y))
elif choice == 4:
    print(x,"/",y,"=",div(x,y))
else:
    print("Invaid choice")