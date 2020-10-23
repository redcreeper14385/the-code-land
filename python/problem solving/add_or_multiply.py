# -*- coding: utf-8 -*-

def menu():
    a = 0
    while(a!=3):
        print("Option 1: Multiply the two numbers")
        print("Option 2: Add up the two numbers")
        print("Option 3: Leave")
        try:
            a = int(input("Type the option you want: "))
        except ValueError:
            print("You didn't put a number")
        else:
            try:            
                if a==1:
                    b = int(input("Type it your first number: "))
                    c = int(input("Type it your second number "))
                    multiply = b * c
                    print(multiply)
                if a==2:
                    b = int(input("Type it your first number: "))
                    c = int(input("Type it your second number "))
                    add = b + c
                    print(add)
            except ValueError:
                print("You didn't put a number")
    print("Bye") 
    
 
if __name__ == '__main__':
    menu()
    

                 