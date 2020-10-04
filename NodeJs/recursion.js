/*
* About recursion
*
* Recursion is a function that calls itself to save code, it is used in a lot of commonly used applications like a antivirus.
* For example it can be used to browse through folders by going into a folder and going into every folder in that folder and so on (this is what a antivirus would do).
*
* In this example we will use recursion to do some simple maths to get an idea of how to use a function that calls itself.
*/

// We will start with 2 numbers, a 1 and a 2
let firstNumber = 1;
let secondNumber = 2;

// We don't want it to end up in a endless loop so we will keep track of how many times we called the function
let loopCount = 0

// A function only works when it is being called, so that is what we do here
recursiveMaths(firstNumber, secondNumber);



// This is our recursive function that will do the maths.
function recursiveMaths(firstNumber, secondNumber) {
    // We will only run this function 50 times for now, so if it exceeds 50 we stop the code
    if (loopCount > 50) return;

    // We add up both the first and second number to create a new variable named newNumber
    let newNumber = firstNumber + secondNumber;

    // We no longer need the first number, so we replace it with the second number
    firstNumber = secondNumber;

    // By using ++ we add 1 to the counter
    loopCount++;

    // We want to see what number is being generated, so we log it in the console
    console.log(newNumber);

    recursiveMaths(secondNumber, newNumber);
}