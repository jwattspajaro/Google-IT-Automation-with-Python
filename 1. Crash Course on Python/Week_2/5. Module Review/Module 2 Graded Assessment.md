###¡Felicitaciones! ¡Aprobaste!
### Calificación recibida 100 %
Calificación del último envío 100 %
Para Aprobar 80 % o más
1.
#### Pregunta 1
Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

1 / 1 punto
``` PYTHON
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

``` 
✅ Correcto
    Well done! You're breezing through the if-else clauses!

2.
#### Pregunta 2
What's the value of this Python expression: "big" > "small"

1 / 1 punto

 ⬜ True


☑️  False


 ⬜ big


 ⬜ small

 ✅Correcto
    You nailed it! The conditional operator > checks if two values are equal. The result of that operation is a boolean: either True or False. Alphabetically, "big" is less than "small".

3.
#### Pregunta 3
What is the elif keyword used for?

1 / 1 punto

 ⬜  To mark the end of the if statement


☑️ To handle more than two comparison cases


⬜  To replace the "or" clause in the if statement


 ⬜  Nothing - it's a misspelling of the else-if keyword

 ✅ Correcto
You got it! The elif keyword is used in place of multiple embedded if clauses, when a single if/else structure is not enough.

4.
#### Pregunta 4
Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.

1 / 1 punto
``` PYTHON
def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass

``` 
✅ Correcto
    Good job! You're getting the hang of it!.

5.
Pregunta 5
What's the value of this Python expression: 11 % 5?

1 / 1 punto

⬜ 2.2


⬜ 2


☑️  1


⬜ 0

 ✅  Correcto
Excellent! "%" is the modulo operator, which returns the remainder of the integer division between two numbers. 11 divided by 5 equals 2 with remainder of 1.

6.
#### Pregunta 6
Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.

Specifically:

If both the last_name and the first_name parameters are supplied, the function should return like so:

``` PYTHON
print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella
If only one name parameter is supplied (either the first name or the last name) , the function should return like so:
```
12
print(format_name("Adele", ""))
Name: Adele
or

``` PYTHON
print(format_name("", "Einstein"))
Name: Einstein
Finally, if both names are blank, the function should return the empty string:
```
``` PYTHON
print(format_name("", ""))
``` 
Implement below:

1 / 1 punto
``` PYTHON
def format_name(first_name, last_name):
	# code goes here
	string = 'Name: ' + ', '.join([name for name in [last_name, first_name] if name]) if any([last_name, first_name]) else ''
	return string
print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"
```

✅Correcto
Awesome! You're getting the hang of the multiple and
embedded "if" clauses!

7.
Pregunta 7
The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.

1 / 1 punto
``` PYTHON
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))

``` 
✅Correcto
You got it! You've figured out how to use an elif clause,
well done!

8.
Pregunta 8
What’s the output of this code?

``` PYTHON
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))
``` 
1 / 1 punto
10
✅Correcto
You nailed it! We’re calling the sum function 3 times: returning 3, then 7, then adding up 3 plus 7 for the total of 10.

9.
Pregunta 9
What's the value of this Python expression?
``` PYTHON
((10 >= 5*2) and (10 <= 5*2))
``` 
1 / 1 punto

True


False


10


5*2

Correcto
Right on! When using the "and" operator, a statement is True if both parts of the conditional are True.
