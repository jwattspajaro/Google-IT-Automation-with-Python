### What is a while loop
Pregunta

``` PYTHON
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))
``` 
How many times will "Not there yet" be printed?
----
### Why Initializing Variables Matters
In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?
``` PYTHON
current=0
def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

``` PYTHON
Here is your output:
3
2
1
Zero!

You nailed it! By initializing the current variable you got
the function to behave correctly.
