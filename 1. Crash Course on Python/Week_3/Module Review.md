### ¡Felicitaciones! ¡Aprobaste!
Calificación recibida 100 %
Calificación del último envío 100 %
Para Aprobar 80 % o más
1.
#### Pregunta 1
Fill in the blanks of this code to print out the numbers 1 through 7.

1 / 1 punto
``` PYTHON
number = 1
while number <= 7:
	print(number, end=" ")
	number += 1
```
Correcto
Nice job! You're really getting the hang of what goes into
the while loops!

2.
#### Pregunta 2
The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.

1 / 1 punto
``` PYTHON
def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter
```
✅Correcto
Great job! You're working the "for" loops the way they're
supposed to be done!

3.
#### Pregunta 3
Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

1 / 1 punto
``` PYTHON
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n >= 1):
		count += 1
		n = n / 10
	return count
	
print(digits(25))   # Should print 2

```
✅Correcto
Woohoo! You've cracked the code of writing code!

4.
#### Pregunta 4
This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

1 2 3 

2 4 6 

3 6 9

1 / 1 punto
``` PYTHON
def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
``` 
✅Correcto
Awesome! You've stepped up to the challenge of one of the
more complex coding practices, nested loops!

5.
#### Pregunta 5
The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

1 / 1 punto
``` PYTHON
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:

```
✅Correcto
You nailed it! You've figured out all of the situations that
need to be considered!

6.
#### Pregunta 6
The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

1 / 1 punto
``` PYTHON
def even_numbers(maximum):
	return_string = ""
	for x in [num for num in range(1, maximum+1) if num % 2 == 0]:
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2

```
✅Correcto
Woohoo! You remembered all of the elements of the range of
the for-loop, well done!

7.
#### Pregunta 7
The following code raises an error when executed. What's the reason for the error?

``` PYTHON
def decade_counter():
	while year < 50:
		year += 10
	return year

1 / 1 punto

⬜ Incrementing by 10 instead of 1


☑️ Failure to initialize variables


⬜ Nothing is happening inside the while loop


⬜ Wrong comparison operator

Correcto
Well done! The variable year needs to be initialized prior to being used in the while loop.

8.
#### Pregunta 8
What is the value of x at the end of the following code?

12
for x in range(1, 10, 3):
    print(x)

1 / 1 punto
7
✅Correcto
You got it! The upper limit of a range isn’t included, which means that the loop stops before reaching it. The increment is 3, so the loop stops when x reaches 7.

9.
#### Pregunta 9
What is the value of y at the end of the following code?

123
for x in range(10):
    for y in range(x):
        print(y)

1 / 1 punto
8
✅Correcto
Great job! The upper limit of a range isn’t included, which means that the outer loop goes up to 9, so the highest upper limit for the inner loop is 9, which is also not included.

10.
#### Pregunta 10
How does this function need to be called to print yes, no, and maybe as possible options to vote for?

1234
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)


1 / 1 punto

votes("yes", "no", "maybe")


votes(yes, no, maybe)


votes([yes, no, maybe])


votes(['yes', 'no', 'maybe'])

✅Correcto
Excellent! This function is looking for one argument, and the list of strings is just one argument. 
