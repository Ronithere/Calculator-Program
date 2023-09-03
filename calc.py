#created by - ronit
#github username - Ronithere
from time import sleep 
def menu():
    print "Welcome to calculator program by Ronit"
    sleep(1)
    print " "
    print "your calculation options are: "
    print " "
    print "1) +"
    print "2) -"
    print "3) x"
    print "4) /"
    print "5) Quit"
    print " "
    return input ("which option you want: ")
    
def add(a,b):
    print a, "+", b, "=", a + b
    
def sub(a,b):
    print b, "-", a, "=", b - a
    
def mul(a,b):
    print a, "*", b, "=", a * b
    
def div(a,b):
    print a, "/", b, "=", a / b
    
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        print("wait...")
        sleep(2)
        add(input("Tell the first numbre to add: "),input("Now tell second number to add with: "))
        print" "
        loop = 0
    elif choice == 2:
        print("wait...")
        sleep(2)
        sub(input("Tell the first numbre to Subtract from : "),input("Now tell second number to subtract with: ")) 
        print" "
        loop = 0
    elif choice == 3:
        print("wait...")
        sleep(2)
        mul(input("Tell the first numbre to Multiply : "),input("Now tell second number to multiply with: "))
        print" "
        loop = 0
    elif choice == 4:
        print("wait...")
        sleep(2)
        div(input("Tell the first numbre to Divide : "),input("Now tell second number to divide with: "))
        print" "
        loop = 0
    elif choice == 5:
        loop = 0
        print" "
print "Program ended"
