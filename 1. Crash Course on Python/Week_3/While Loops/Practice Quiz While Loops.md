### Felicitaciones! ¡Aprobaste!
Calificación recibida 100 %
Para Aprobar 80 % o más
1.
#### Pregunta 1
What are while loops in Python?

1 / 1 punto

☑️ While loops let the computer execute a set of instructions while a condition is true.


 ⬜ While loops instruct the computer to execute a piece of code a set number of times.


 ⬜ While loops let us branch execution on whether or not a condition is true.


 ⬜ While loops are how we initialize variables in Python.

✅ Correcto
	Right on! Using while loops we can keep executing the same group of instructions until the condition stops being true.

2.
Pregunta 2
Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.

1 / 1 punto
``` PYTHON
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
```
✅Correcto
	You nailed it! You've got the code to print all the right
	prime factors. Well done!

3.
Pregunta 3
The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.

Note: Try running your function with the number 0 as the input, and see what you get!


1 / 1 punto
``` PYTHON
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while  n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  
```
✅ Correcto
	Awesome! You fixed a tricky error that was hard to find and
	the function now behaves correctly.

4.
Pregunta 4
Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.

1 / 1 punto

``` PYTHON
def sum_divisors(n):
  sum, num = 0, 1
  while num < n:
    if n % num == 0: 
      sum += num
      if num > n//2: 
       pass
    num += 1
  # Return the sum of all divisors of n, not including n
  return sum

``` 
✅ Correcto
	Well done, you! You've written a complex while loop and got
	Python to do the work for you.

5.
Pregunta 5
The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.

1 / 1 punto
``` PYTHON
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))

``` 
✅Correcto
	Excellent! You completed the multiplication table with all
	of the required criteria, and it looks great!
