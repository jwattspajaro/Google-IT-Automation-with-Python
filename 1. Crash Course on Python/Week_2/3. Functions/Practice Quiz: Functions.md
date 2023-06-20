### ✅¡Felicitaciones! ¡Aprobaste!
Calificación recibida 100 %
Para Aprobar 80 % o más
1.
#### Pregunta 1
1. This function converts miles to kilometers (km).

2. Complete the function to return the result of the conversion

3. Call the function to convert the trip distance from miles to kilometers

4. Fill in the blank to print the result of the conversion

Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result


1 / 1 punto
``` PYTHON
12345678910111213141516
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile
convert_distance(55)
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
``` 

✅Correcto
    Woohoo! You’ve figured out how to make the functions do what
    they need to do, and remembered some things from the
    previous lessons. Way to go!.

2.
#### Pregunta 2
1. This function compares two numbers and returns them in increasing order.

2. Fill in the blanks, so the print statement displays the result of the function call in order.

3. Hint: if a function returns multiple values, don't forget to store these values in multiple variables

1 / 1 punto
``` PYTHON
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
``` 

 ✅Correcto
Nice! You remembered how to accept multiple return values
from a function. You’re ready for the next lesson!

3.
#### Pregunta 3
What are the values passed into functions as input called?

1 / 1 punto

 ⬜Variables


 ⬜Return values


☑️ Parameters


 ⬜Data types

 ✅Correcto
Nice job! A parameter, also sometimes called an argument, is a value passed into a function for use within the function.

4.
Pregunta 4
Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.

1 / 1 punto
``` PYTHON
def lucky_number(name):
  number = len(name) * 9
  return  "Hello " + name + ". Your lucky number is " + str(number)

	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
``` 
 ✅Correcto
Way to go! The function now returns the message, for the
calling line to use it in any way it wants to.

5.
Pregunta 5
What is the purpose of the def keyword?

1 / 1 punto

☑️ Used to define a new function


 ⬜  Used to define a return value


 ⬜  Used to define a new variable


 ⬜  Used to define a new parameter

✅Correcto
Awesome! When defining a new function, we must use the def keyword followed by the function name and properly indented body.
