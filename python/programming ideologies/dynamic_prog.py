import time
'''
This snippet of code explains the method of "Dynamic Programming".
It is a simple and intuitive yet very efficient way of improving performance of an algorithm.

The problem statement is to calculate the nth-Fibonacci Number
Fibonacci Numbers are a sequence in which each number is equal to the sum of the preceeding two numbers

The first 10 Fibonacci Numbers are:
	1,2,3,5,8,13,21,34,55,89... 

We will write two code snippets, one without dynamic programming, and one with it; an dsee how they compare.
'''

#Code1: Without Dynamic Programming--Naive
def naive_nth_fibo(n):
	if(n<=2):
		return n
	else:
		return naive_nth_fibo(n-1)+naive_nth_fibo(n-2)

'''
This code is very simple to understand. However, it is very slow. (Try to see the time for large values of n!)

Lets see what the program does to find, say, the 5th Fibonacci Number.
To find F5, it goes into the else case and finds the value of F4 and F3.
Similarly, for F4, it tries to find the values of F3 and F2.

However, notice that the value of F3 is being computed TWICE!
	1) Once in F5
	2) Again in F4

This may seem small because n=5, but try to see how many recomputations are done for n=15, and the problem is evident.
Therefore, to reduce re-computations, we can store the values of F3, and use them directly when needed.
This is done below.
'''

#Code2: Efficient Algorithm
def faster_fibo(n):
	ith_fibo=[0]*n
	ith_fibo[0]=1
	ith_fibo[1]=2

	for i in range(2,n,1):
		ith_fibo[i]=ith_fibo[i-1]+ith_fibo[i-2]

	return ith_fibo[n-1]

'''
This is Dynamic Programming. Put simply, its just storing the values which might be computed many times in the algorithms, and using them when needed.
Notice that this is much faster compared to the original algorithm.
'''

start1 = time.time()
val1=naive_nth_fibo(40)
end1=time.time()

start2 = time.time()
val2=faster_fibo(40)
end2=time.time()

print(str(val1) + " --- Time taken by first algorithm: " + str(end1-start1))
print(str(val2) + " --- Time taken by second algorithm: " + str(end2-start2))

'''
On my PC, the first algorithm took 13 seconds, whole th esecond one took nearly 10 Microseconds to compute, so the difference is HUGE.
''' 