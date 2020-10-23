#include <iostream>
using namespace std;

int main(){
/*
	The aim of this code is to help beginners get used to, and understand the importance of "pointers" in c++.
	Let's get started!

	When a variable is declared in c++, on your computer, some memory is allocated to storing that memory.
	A "pointer" is a variable which simply points to where the allocated memory is present.
*/

	int var = 50;

//	Suppose we wanted to get the address of `var`. For this we use the "Referencing Operator", '&'.
//	That is just fancy jargon for "An operator which gives me the address of the variable".
//  The address is of the form '0x7ffc204e0914', a hexadecimal number. You dont need to worry if you dont understand what this means.

	cout << "The variable 'var' is stored at the location: " << &var << endl;

// 	Now, if we wanted to store the address of `var` into a variable, we would have to first create a "pointer" of type int.
//	This is done by using '*' before declaring the name of the pointer.

	int *add;

//  This means that `add` is a pointer which points to the address of a variable of type int.
//  We can assign it the value of the address of var, and we will have a variable pointer pointing at var!

	add = &var;

//  Now suppose we wanted to access the value at the address which the pointer `add` is pointing at.
//	For this, we use the "Dereferencing Operator", '*' 
//	Fancy Jargon for "Gimme the value of the variable!"

	cout << "The value of the stored data pointed by 'add' is: " << *add << endl;

/*
	Pointers usually see usage in classes and data structures similar to arrays.
	Because this is suppsed to be a beginner's guide, I will be dealing with arrays.

	1)Arrays
		The best part about an array is that all of its pointers are consecutive in nature.
		Meaning that if `p1` is a pointer to the start of the array, `p1+1` is the pointer to the second element in the array and so on.

		This has been shown below.
*/

	int arr[5];
	arr[0] = 1; arr[1] = 2; arr[2] = 3; arr[3] = 4; arr[4] = 5;

//		Create a pointer to the start of the array in a similar way to the one done above.

	int *ptr;
	ptr = arr;		//Points to the start of the array!

//		Show that they are, in fact, consecutive

	cout << endl;
	cout << "The first element of the array found by pointers is: " << *ptr << endl;
	cout << "The second element of the array found by pointers is: " << *(ptr+1) << endl;

//	Notice that we've done `ptr=arr`, and not `ptr=&arr`. This is because for arrays, the operator '[]' acts similar to '&' for normal variables.
//	Meaning that 'arr' is a pointer, and printing the values of *arr, *(arr+1) would've worked as well!

	cout << endl;
	cout << "The first element of the array found by array is: " << *arr << endl;
	cout << "The second element of the array found by array is: " << *(arr+1) << endl;

/*
	If you feel confident with the implementation of what has been taught till now, I highly reccomend learning the usage of pointers
	with classes, as they find the most use there, and mistakes made using pointers can be tough to debug.
*/

	return 0;
}