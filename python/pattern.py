# this is a very basic code explaining basics of pattern printing.
# if input is 3 it will print 
# 333
# 333
# 333

N = int(input())             # asks user to input a number 
i=1                          # variable to print row 
while i<=N:                  # loop that will print rows 
    j=1                      # variable to print columns
    while j <= N:            # whatever gets printed because of i is multipied here into columns
        print(N, end="")     # our entered number is getting printed and end keyword appends space instead of newline
        j=j+1                # increasing j to move to next column
    print()                  # print statement to move cursor to new line as end keyword appends space
    i=i+1                    # increasing i to move to next row
    
