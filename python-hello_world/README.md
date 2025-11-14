This repository for hosting scripts and task resolutions in project "Python - Hello, World.
Requirements for resolving tasks.
Python Scripts:
-Allowed editors: vi, vim, emacs
-All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
-All your files should end with a new line
-The first line of all your files should be exactly #!/usr/bin/python3
-A README.md file at the root of the repo, containing a description of the repository
-A README.md file, at the root of the folder of this project, is mandatory
-Your code should use the pycodestyle (version 2.7.*)
-All your files must be executable
-The length of your files will be tested using wc


Tasks list in directory "python-hello_world" is below:

Task "0. Hello, print" - file: 2-print.py.
>>> Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.Note: Use the function print.

Task "1. Print integer" - file: 3-print_number.py.
>>>Complete in order to print the integer stored in the variable number, followed by Battery street, followed by a new line. 
<code starts>
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE"
<Code ends>
- The output of the script should be:
	*the number, followed by Battery street,
	*followed by a new line
-You are not allowed to cast the variable number into a string
-Your code must be 3 lines long
-You have to use f-strings tips

Task "2. Print float" - file: 4-print_float.py.
>>>Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
<Code starts>
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
<Code ends>
-The output of the program should be:
	*Float:, followed by the float with only 2 digits
	*followed by a new line
-You are not allowed to cast number to string
-You have to use f-strings

Task "3. Print string" - file: 5-print_string.py.
>>>Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
<code starts>
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
<code ends>
-The output of the program should be:
	*3 times the value of str
	*followed by a new line
	*followed by the 9 first characters of str
	*followed by a new line
-You are not allowed to use any loops or conditional statement
-Your program should be maximum 5 lines long

Task "4. Play with strings" - file: 6-concat.py
>>>Complete this source code to print Welcome to Holberton School!
<code starts>
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"Welcome to {str1}!")
<code ends>
-You are not allowed to use any loops or conditional statements.
-You have to use the variables str1 and str2 in your new line of code
-Your program should be exactly 5 lines long

Task "5. Copy - Cut - Paste" - file: 7-edges.py
>>>Complete this source code
<code starts>
#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
<code ends>
-You are not allowed to use any loops or conditional statements
-Your program should be exactly 8 lines long
-word_first_3 should contain the first 3 letters of the variable word
-word_last_2 should contain the last 2 letters of the variable word
-middle_word should contain the value of the variable word without the first and last letters

Task "6. Create a new sentence" - file: 8-concat_edges.py.
>>>Complete this source code to print object-oriented programming with Python, followed by a new line.
<code starts>
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str)
<code ends>
-You are not allowed to use any loops or conditional statements
-Your program should be exactly 5 lines long
-You are not allowed to create new variables
-You are not allowed to use string literals

Task "7. Easter Egg" - file: 9-easter_egg.py
>>>Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)


