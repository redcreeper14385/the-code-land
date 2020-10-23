# Contributed by Parjanya HK

# Palindrome Program using inbuilt Method:

str=input(("Enter a string:"))
if(str==str[::-1]):
      print("The entered string is a palindrome")
else:
      print("The entered string is not a palindrome")
      
      
''' The same program can be written using a while loop:

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
    
'''
