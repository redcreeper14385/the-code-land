/* 
* NodeJs is a open source JavaScript runtime environment that can be used to run JavaScript outside of a browser. 
* It can be used to create a simple console application, a app for your computer or phone and many other things.
*
* Here we will display 'Hello world' in the console in different ways.
*/

// In JavaScript you can not define what you will put inside of a variable, hence why 'let', 'var' and 'const' are used.
// For now we will stick with a 'const' because this text won't be modified in any way so the variable is a constant (const).
// Also note how you don't need to add a ';' at the end of the line if you continue your code on the next line, you can however still add one if you like, your code will still work
const helloWorld = "Hello world!"

// To display information in the console you need to log it, anything provided within the brackets will be logged.
// For now we will display the variable 'helloWorld'.
console.log(helloWorld)



// Sometimes you don't have all the information ready yet at the start of the code so it gets added to an array.
// To create a empty array you need to create a new variable and making it equal to [].
// In this case we change the variable overtime so we need to use a 'var' or 'let', for now we will stick with a let because this is the prefered variable type by JavaScript
let array = []

// Now we want to fill it with data. This is done by pushing a value something to that array.
array.push("Hello")
array.push("world!")

// We filled the array with data, but we want to display it as a string. 
// To convert a array to a string you need to join everything. This is done by using 'array.join()' and specifying what to join it with.
// In this case we will use a space to seperate the words. You can run this code within the brackets of the console.log and it will still work.
console.log(array.join(" "))


/* Running this code will log the same thing twice, but it is being generated in a different way. */