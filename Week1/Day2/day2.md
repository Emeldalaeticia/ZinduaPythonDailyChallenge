Palindrome Challenge

This code reads a file called eng_words.txt that contains a list of English words, and finds all the palindromic words in the list. Palindromic words are words that read the same forwards and backwards, like "racecar" or "level".
The code checks each word in the list to see if it is a palindrome by reversing the word and checking if it is the same as the original word. If the word is a palindrome, the code adds it to a list of palindromic words.
Once all the words in the list have been checked, the code prints out all the palindromic words that were found, along with the message "is palindromic".

After finding the palindromic words using the find_palindromes function, the code creates a new file called palindromesNew using the with open('palindromes', 'w') as f statement. 
The w argument specifies that we want to write to the file.
The code then uses a for loop to iterate over the palindromic words found, and writes each word to the new file using the f.write() method. 
The '\n' character at the end of the string adds a new line after each word.




Fibonacci Sequence challenge

A sequence of numbers where a number is the sum of the 2 numbers that came before it. The sequence first digits are 0 and 1.
We have to take this into account that the first digits are 0 and 1.

The fibonacci formula is

f(n) = f (n-1) + f (n-2) for n >= 0
I get the sequence by defining a function called fibonacci(n), which takes an input value n and returns the n-th Fibonacci number.
The function first checks if n is 0 or 1 and returns 0 or 1 respectively if this is the case. 
Otherwise, the function calculates the n-th Fibonacci number as the sum of the n-2-th and n-1-th Fibonacci numbers, which are themselves calculated by recursively calling the fibonacci function.
The code then prints out the first 12 Fibonacci numbers using a for loop that iterates through the range 0 to 11 and passes each value to the fibonacci function.
The fibonacci function then returns the corresponding Fibonacci number, which is printed to the console
