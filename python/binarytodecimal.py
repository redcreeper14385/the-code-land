#convert binary number to a decimal number

def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal = i = n = 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print("The decimal form of the number is", decimal)     
      
if __name__ == '__main__': 
    x = int(input("Enter a binary number: "))
    binaryToDecimal(x)
