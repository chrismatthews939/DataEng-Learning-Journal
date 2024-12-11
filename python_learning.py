
# Python Learning
'''
—————

*Dictionaries*

—————

Key value pairs, can be lots of values
Wrapper is {}
Can have list inside dict
'''
student = {'name': 'John', 'age': 35, 'courses': ['math', 'science']}

#To get single key
Print(student[name])

#Add a not found for non existent keys
Print(student.get(phone, 'Not Found'))

#To update a key you can just change it (update from John to Jane)
student[name] = 'Jane'

#Or to do different types of changes use update
student.update({'name': 'Jane', 'age': 30, 'phone': 555-555})

#To delete key
del student[age]

#To show all keys
student.keys()

#For values
.values()

#For everything
.items()

#To loop through a dictionary will only loop through keys unless you specify .items()

for key in student:
   print(key)

for key in student.items():
   print(key)

#To loop through both keys and values
for key, value in student.items():
   print(key, value)
'''
—————

* __name__ == __main__*

—————

__name__ == __main__
When you see this it's a check to know if it's directly running the file or is it being imported from somewhere because it's difficult to know otherwise. Allows you to create conditions to run or not run an imported file.

Python sets some things in the background and always calls the first program __main__

—————

*classes*

—————

Class is basically a category to store data

For example:
'''
class Employee:
     # init is initialise
     # by default the first instance is passed so we call it self
     # you can call it anything but self is standard practice
     def __init__(self, email, name, pay):
           self.email = email
           self.first_name = first_name
           self.last_name = last_name
           self.pay = pay
# self. Doesn't need to match but it's easier to read. In this case emp1/2 is the self element
           

emp1 = Employee(emp1.com, John, Jones, 50000)
emp2 = Employee(emp2.com, James, Smith, 60000)

#Groups all info under the employee class
'''
—————

*methods*

—————

methods perform an action to our class
Let's consider the above class

You could have a method for full name inside the employee class
'''
def full_name(self):
    return '{} {}'.format(self.first_name,self.last_name)

#One useful tip is that you can put functions inside the class and they will be executed for things in the class

#For example putting

no_of_employees = 0

#In the class will set the no to 0

#But then under the init method you put

Employee.no_of_employees += 1

#This was every time a new employee is entered into the class you get an extra 1 added to the total
'''
—————

*sub classes and inheritance*

—————

A sub class is a class that inherits some bits from the main class

For example our employee class from my class example has things like name or email that we might want to include in a manager class. Rather than write it all again we can have it as a manager class 
'''
class Employee:
  
     def __init__(self, email, name, pay):
           self.email = email
           self.first_name = first_name
           self.last_name = last_name
           self.pay = pay

class manager(Employee):
      pass
# this alone will have everything in the Employee class

#We can also change things in the subclass to have a new value
'''
—————

*error handling*

—————

Use try and except to pass error messages
'''
try:
   f = open(file.txt)
except Exception:
   print('Error opening file')

# The issue with the above is any error will be caught as a file not found
# To catch specific error you can pass those

try:
   f =open(file.txt)
except FileNotFoundError:
   print('Error opening file')

# Can also have more than one
try:
   f = open(file.txt)
   var = badvar
except FileNotFoundError:
   print('Error opening file')
except Exception:
   print('some other error')

# Can also pass some name to list the errors
try:
   f = open(file.txt)
   var = badvar
except FileNotFoundError as e:
   print(e)
except Exception as e:
   print(e)

# This will result in Err1, Err2 so you still know which bit caused the error

# Can also have messages for passed code
try:
   f = open(file.txt)
   var = badvar
except FileNotFoundError as e:
   print(e)
except Exception as e:
   print(e)
else:
   print(f.read())
   f.close

# There is also finally clause. Useful for closing databases etc

try:
   f = open(file.txt)
   var = badvar
except FileNotFoundError as e:
   print(e)
except Exception as e:
   print(e)
else:
   print(f.read())
   f.close
finally:
   print('Executed')

#Lastly can also manually pass errors

try:
   f = open(file.txt)
   if name == file.txt:
      raise Exception
except FileNotFoundError as e:
   print(e)
except Exception as e:
   print('Error!')
else:
   print(f.read())
   f.close
finally:
   print('Executed')

#This will find the Exception block for a specific thing you want to find

#Another example to make sure user inputs a number to add to their balance

balance = 99

while True:
    try:
        num = float(input('Deposit: ')) #convert user input to float
        break # finish it input is number
    except ValueError:
        print('must be a number')

balance += num
print(f'Balance = (balance)')

'''
—————

*list comprehension*

—————

Easier way to manage lists

So you could create a list with standard loop
'''
nums = [1,2,3]
new_list = []
for n in nums:
     new_list.append(n)

#Or you can you a list comprehension

new_list = [n for n in nums]

#Or you can use map and lambda but more often list comprehension is better because it's easier to read

new_list = map(lambda n: n, nums)

#Example of the above three to show even numbers only

nums = [1,2,3]
new_list = []
for n in nums:
     if n%2 == 0:
            new_list.append(n)

new_list = [n for n in nums if n%2 == 0]

#For lambda we use filter not map

new_list = filter(lambda n: n%2 == 0, nums)

#For a more complicated example:
#Want to have a letter number pair for letter abc and numbers 0123
#All combinations a0 a1 a2 a3 b1 etc

#Normal method

mylist = []
for letter in 'abcd':
     for num in range(4):
          mylist.append((letter, num))

#List comprehension method

mylist = [(letter, num) for letter in 'abcd' for num in range(4) ]

#Can do the same thing making a dictionary (key value pairs) instead of list

#Use zip function

name = ['Bruce', 'Peter']
hero = ['Batman', 'Spiderman']

mydict = {name: hero for name, hero in zip(hero, names)}

#This puts name with hero

#Can filter things out as well

mydict = {name: hero for name, hero in zip(hero, names) if name != 'Peter'}

#Can also do set comprehension
#Set is a list of unique things

#So set of this list
nums = [1123344555]
#Would show 12345

myset = {n for n in nums}
'''
—————

*generators*

—————

A generator is a function or expression that will process a given iterable one object at a time, on demand. A generator will return a generator object, which can be cast as a list or some other data structure as appropriate.

Instead of a function to square numbers in a list like this
'''
def square_number(nums):
    result = []
    for i in nums:
          result.append(i*i)
    return result

my_nums = squared_number(1,2,3,4)

#You could use a generator by removing the results bit and use yield keyword to make it a generator

def square_number(nums):
    for i in nums:
          yield(i*i)
    return result

my_nums = squared_number(1,2,3,4)

#The results will only be looped one at a time
#You'll need to use next to see each number squared

print next(my_nums)

#You could use a loop to see all nums

for num in my_nums:
      print num

#A generator is advantageous because you don't need to start with an empty list and append to it

#If I used a list comprehension instead of the function like this

my_nums = [x*x for x in [1,2,3,4]]

#To change to a generator swap the list brackets for parenthesis

 my_nums = (x*x for x in [1,2,3,4])

for num in my_nums:
      print num

#For a list like this performance is negligable but because a list is held in memory and a generator isn't it's much more efficient with big datasets
'''
—————

*variable scope*

—————
'''
x = 'global x'

def test():
   y = 'local y'
   print(x)

test()
print(y)

#Because x is defined explicitly it will be found in the function. The function will look for an x value and then when it can't find one it will default to the global one.

#However printing y outside the function won't work because it's only a local variable and doesn't cost outside the function.

'''
—————

*sorting lists*

—————
'''
list = [4,2,1,3]
sorted_list = sorted(list) #put list in asc order

# Can also do
list.sort()

# However this doesn't give you a new list it's just a method on the old list. The method only works on lists . You couldn't have a tuple (tuples are like lists but are immutable, so can't be changed after creation) and do tuple.sort()

#For desc add reverse = True

sorted_list = sorted(list, reverse=True)

#If your list has negative values and you want to sort by absolute you can use a key value

list = [-6,-5,4,2,1,3]
sorted_list = sorted(list key=abs)

1,2,3,4,-5,-6

#  If you try and sort something without an obvious sorting type such as a name in a list it will error

# To sort a dictionary key you can create a variable with the key and then pass that through the sort

# With a dictionary called employees with one of the keys being employee salaries you could do:

# anything passed will filter the salary key
def e_sort(emp):
    return emp.salary

sorted_by_salary = sorted(employees key=e_sort reverse=True)

# However with something this short you could pass an anonymous lambda function

sorted_by_salary = sorted(employees key=lambda x: x.salary reverse=True)

# There is also a function for this

from operator import attrgetter
sorted_by_salary = sorted(employees key=attrgetter('salary') reverse=True)

'''
—————

*slicing lists*

—————
'''
my_list = [1,2,3,4,5]

#Can do negative indexes

print(my_list[-1]) #prints 5

#Indexes always start at 0

print(my_list[0]) #prints 1

print(my_list[0:3]) #prints range 1,2,3,4

print(my_list[2:3]) #prints range 3,4

print(my_list[2:]) #prints range 3,4,5

print(my_list[:-1]) #prints range 1,2,3,4

#Can also step through values

print(my_list[0:3:2]) #prints every second value in range 2,4

#Can do the same with strings
my_string = 'Hello'

print(my_string[::-1] #prints entire string but the step -1 does it in reverse. Prints 'olleH'

print(my_string[1:2] #prints 'el'

'''
—————

*string formatting*

—————
'''
person = {'name': 'Jen', 'age': 23}

# Beginner method is concatenation
sentence = 'My name is '+person.['name']

# Better to use {} as placeholders and then run format method. Much easier to read

sentence = 'My name is {} and I'm {}years old'.format(person.['name'],person.['age'])

# You can also number the placeholders. Numbers are good to create things like HTML code where you might want to start and finish code with

sentence = 'My name is {0} and I'm {1}years old'.format(person.['name'],person.['age'])

# The other way to write this is swap where you put the variables. Just bit easier to write

sentence = 'My name is {0} [name]and I'm {1}[age]years old'.format(person)

# This works with class elements as well

Dictionary example
person = {'name': 'Dave', 'age': 23}

sentence = 'My name is {name} and I'm {age years old'.format(**person)

'''
—————

*Slicing with numbers*

—————
'''

for i in range(1,5):
    sentence = 'The value is {}'.format(i)
    
# To pad a leading zero use a colon (: is for formatting). 02 is padding to two places (02,03,04 etc). 03 is padding to three places (002,003,004 etc).

for i in range(1,5):
    sentence = 'The value is {:02}'.format(i)

# For two decimal places use .2f, for three .3f

sentence = 'The value is {:.2f}'.format(i)

# For comma brakes e.g 1,000,000 put a comma

sentence = 'The value is {:,}'.format(i)

# Can also format dates this way. Check online documentation for specific formats such as day of the week

import datetime
my_date = datetime.datetime(2024, 11, 12, 10, 20)

sentence = 'The time is {:%B %d %Y}'.format(my_date)

'''
—————

*functions*

—————

Best practice to have lots of small reusable functions and pass them than one complicated big one

Type annotations (being explicit with data being worked with)

Instead of passing something ambiguous into a function such as
'''
def upper_everthing(elements):
      Return [element.upper() for element in elements]

# This would break with a number

# Instead use type annotations to fix it

def upper_everthing(elements: list[str]) -> list[str]:
      Return [element.upper() for element in elements]

# This tells the user exactly what's happening. You input a string and the return is a string. It's good for setting constraints and also like documentation.

# mypy is a good pip install addon to have in before to flag bad data types

'''
—————

*executing functions*

—————
'''
# The below passes in greeting and name

def hello_func(greeting, name='you'):
    return '{}, {}'.format(greeting, name)

# You can leave name blank and it will default to 'you' or overwrite it like the example below

print(hello_func('Hi', name = 'John'))

'''
—————

*positional key word arguments*

—————
'''
# Use if you don't know the number of arguments to be passed. The above example won't work if more are passed.

# *args are positional arguments, like greeting above, **kwargs are key word arguments, like name above

def student_info(*args, **kwargs):
     print(args)
     print(kwargs)

student_info('Math', 'Art', name = 'John', age = 22)

Running this will print the args Math and Art
And print the kwargs Name John and Age 22

If you had variables for the list and dictionary like this

course = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(course, info)

# This won't work because it will put all together. To get Python to unpack as a list and then dictionary add the *'s. This tell Python to unpack each bit.

student_info(*course, **info)

'''
—————

*lambda*

—————

If you have a simple function you only need to use once you can use lambda. It's a short function that can't be used elsewhere but easier to write as a one off
'''
So instead of
def add(x,y):
    return x+y
print(add(1,2))

Use
print((lambda x,y: x+y)(1,2))

# First x and y is the same as the ones after the def 
#  Second one is the return 

'''
—————

*map*

—————
'''
# Map takes a function and returns an integrator that applies the function to every item of iterable

# If we had a function to make numbers even by finding odd numbers and adding 1 

def make_even(num):
     if num%2 == 1:
           return num+1
     else:
           return num

arr = [2,4,3,5]

# If we wanted to apply the function to every number in this list we can do a loop

new_arr = []

for i in arr:
   y.append(make_even(i))
print(new_arr)

# Or we can use map. Map takes the function make_even and then the iterable arr and apply it to each number 

new_arr = map(make_even, arr)

print(new_arr)

# This will make it a funny map format so best to put back at a list

new_arr = list(map(make_even, arr))

# list comprehension can also do this job

new_arr = [make_even(i) for i in arr]

'''
—————

*match case statements*

—————
'''
# used to match what a user puts in to a case. It's like an if statement but for user input

# E.g. if you have a do this or do that function you can ask the user which they want and use the match case statement to run the correct function. In the below match input will prompt the user with 'do this or do that'. If they input this it will match and run def do_this if they don't input that it will run do_that function. The last case has an _ so it will catch a thing else and print invalid.

def do_this():
      print('doing this')

def do_that():
      print('doing that')

match input('do this or do that? '):
      case 'this' :
            do_this()
      case 'that':
            do_that()
      case _:
            print('invalid input')

'''
—————

*first class functions*

—————
'''
# Basically treating a function like any other object or variable

# This means assigning a function to a variable NOT the results of a function

# So for example with the below function to square a number

def square(x):
      return x * x

f = square(5)

print square # returns 'function square'
print f # returns 25

# To set f as the function rather than the result you remove the input and parentheses. The parentheses mean you want to execute the function

f = square

# f is now a first class function. You can use it just like you can use square.

# With this you could pass f as an argument in another function. This is know as higher order functions.

# For example we could create a map function (these exist in Python as standard functions but here we are creating it). This function passes a function and then a list. It runs the function over the list and appends the result to an empty list.

def square(x):
      return x * x

def cube(x):
      return x * x * x

def my_map(func, arg_list):
     result = []
     for i in arg_list:
          result.append(func(i))
     return result

# now we can change the variable and pass a different function

squares = my_map(square, [1,2,3,4,5]
print(squares) # result 1,4,9,16,25

cube = my_map(cube, [1,2,3,4,5]
print(cube) # result 1,8,27, 64, 125

# These are complicated but a simplistic example is

def html_tag(tag):
    def wrap_text(msg):
          print('<{0}>{1}'.format(tag,msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1('a headline')
print_h1('another headline')

# result is
a headline<\h1>
another headline<\h1>

# The first print_h1 variable passes the tag h1
# Then the next one passes the function remembering the tag and runs the message as the msg argument and prints it. Same for the next message.

'''
—————

*closures*

—————

Very similar to first class functions. Basically it's the ability to hold a functions results in memory to be able to execute it independently.
'''

def outer_func():
       message = ('Hi')
       def inner_func():
               print(message)
       return inner_func

my_func = outer_func()
print(my_func)

# This will remember the local variable (message) that was created and can execute it through something else like a function or variable

# A first-class function is any function treated like a value (e.g., passed as an argument or returned from another function), while a closure is a function that remembers variables from its enclosing scope even after that scope has finished executing.

'''
—————

*decorators*

—————
decorators are a follow on from closures but they take a function as an argument, do something and then give a function as a result

The reason for it is it allows for new functionality to be easily passed into our existing functions

The below function passes a function as an argument. Then we create a function called display and pass it through.
'''
def decorator_function(original_function):
     def wrapper_function():
           print('wrapper executed this before {}'.format original_function.__name__)
           return original_function()
     return wrapper_function

def display():
      print('display function ran')

display = decorator_function(display)

display()

# In Python there is a special syntax for decorators using @. We can put this above the function and that tells the computer to pass that function through our decorator function (does the same as the last two lines but easier to read)

@decorator_function
def display():
      print('display function ran')

# You can also chain decorators together

# The main use case is logging. Tracking how often a function has been executed

'''
—————

*loops*

—————
'''
nums = [1,2,3,4,5]

for i in nums:
     if num == 3:
           print('found it!')
           break # breaks loop here
     print(i)

# Returns
# 1
# 2
# found it!

# If we want to skip 3 and not break we can use continue

for i in nums:
     if num == 3:
           print('found it!')
           continue # skips and continues
     print(i)

# Returns
# 1
# 2
# found it!
# 4
# 5

# Loops within loops

nums = [1,2]

for num in nums:
     for letter in ['a', 'b']:
           print(num, letter)

# Returns
# 1a
# 1b
# 2a
# 2b

# If you want to run through a loop a set number of times use range

for i in range(10) # loops 10x. 0 to 9

for i in range(5, 10) # loops from 5 to 9

# While loops
Loops while a condition is true

x = 0

while x < 10:
     print(x)
     x =+ 1

# Can also add a break this the same way. The below now stops at 5

x = 0

while x < 10:
     if x == 5:
            break
     print(x)
     x =+ 1
     
'''
—————

*pythonic*

—————

Being pythonic is writing in a way that is specific to Python code and best practices for clean readable code

Duck typing
If it looks like a duck and walks like a duck then it's a duck. Basically we don't care what our object looks like we just care that it does what we ask it to do

Duck typing brings several advantages to programming in Python. It allows for more flexible and reusable code and supports polymorphism, enabling different object types to be used interchangeably as long as they provide the required interface. This results in simpler and more concise code

For example if we have two classes we can be explicit in how we run them. 

'''
class duck:
    def quack(self):
         print('quack quack')
    
    def fly(self):
         print('flap flap')

class person:
    def quack(self):
         print('I'm quacking like a duck')
    
    def fly(self):
         print('I'm flapping my arms')

def quack_and_fly(thing):
    #not duck types pythonic
    if instance(thing, Duck):
          thing.quack()
          thing.fly()
    else:
          print('this has to be a duck')

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

If we run this we get
quack quack
flap flap
this has to be a duck

# This only runs the duck class because we are checking for that in the if instance

# But duck typing shouldn't care about being explicit. If the function works we should let it pass. 

# Instead replace with
def quack_and_fly(thing):
    #pythonic
     thing.quack()
     thing.fly()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# If we run this it will run both because the functions inside the classes are the same
quack quack
flap flap
I'm quacking like a duck
I'm flapping my arms

# If you were worried about passing the wrong things through you can use a try. This is asking for forgiveness pythonic method instead of explicitly checking each. 

E.g
def quack_and_fly(thing):
   try:
         thing.quack()
         thing.fly()
   except AtrributeError as e:
         print(e)

# Asking for permission not forgiveness (EAFP)
# This is for clean code. Rather than being explicit for everything just use a try block and if it works great.

# E.g for a function to get an index from list
my_list = [1,2,3,4,5]

#not pythonic
if len(my_list) >= 6: #this is asking permission
      print(my_list[5]
else:
      print('the index doesn't exist)

#pythonic
try:
   print(my_list[5]
except IndexError:
      print('the index doesn't exist)

# Not only is this easier to write but the first bit of code will reference the object multiple times where as this will just do it once

# Optimisation trick
# If global variable is passed through a function the function has to check is first which slows performance. To get around this convert it to a local variable inside the function.

# Before
global_variable = 10

def func():
     ans = 0
     for i in range(10000):
           ans =+ global_variable * i
      return ans

func()

# After optimisation
global_variable = 10

def func():
     ans = 0
     local_variable = global_variable
     for i in range(10000):
           ans =+ local_variable * i
      return ans
'''
—————

*sorting algorithms*

—————
'''
# **Insertion sort**
# We do have the built in sort function for this but it's good to know how it works

# Given a list of numbers 

2651
# You start with the number on the left and then move 1 to the right and compare with its left neighbour until it finds its sorted position 

# So the sequence is:
2651
2651
2561
2516
2156
1256 sorted 

# To write this as a script:

def insertion_sort(arr):
    for i in range(1, len(arr)): # loop through array
          j = i
          while arr[j - 1] > arr[j] and j > 0: # if j is greater than its neighbour and j is greater than 0
               arr[j - 1],  arr[j] = arr[j],  arr[j - 1] # swap them over 
               j -= 1 # move to the left after swap

arr = [2, 6, 5, 1]
insertion_sort(arr)
print(arr) # returns 1256

# **Selection sort**
# Selection sort loops through the list and marks which is a lowest number it finds. When it finds that number it swaps it with the one at the start. Then continues with the same from the next number etc

# So the sequence is:
#2651 # swapped 1 with 2 because it's lowest
1652
1256 sorted 

# You can see this is shorter than the version above 

# To write this as a script:

def selection_sort(arr):
    for i in range(0, len(arr)-1): # loop through array
          curr_min_index = i # set a start min
          for j in range(i + 1, len(arr)): # another loop to find new min value
                 if arr[j] < arr[curr_min_index]: # if arr at position j is less than the arr at our curr min index
                         curr_min_index = j # set new min value
          arr[i],  arr[curr_min_index] = arr[curr_min_index],  arr[i] # swap them over same as previous example 

arr = [2, 6, 5, 1]
selection_sort(arr)
print(arr) # returns 1256

# **Merge sort**
# Merge sort using a divide and conquer method, which essentially means breaking the problem down into smaller ones until they become easy to solve. You then combine the solutions to fix the original problem. 

# Has optimal running time
# O(n * log(n))

# Merge sort split the array in half and then sort each half
# Then merge the sorted half's 

# Example array merge sort. Even lists split neater but using an odd n list to show how it works

2654732
# split 
2654   732
# split 
26  54  73  2
# start sorting the pairs 
26  45  37  2
# compares the left elements in each
2456  237
# last merge
223456 sorted

# Example Python code:
def merge_sort(arr):
	if len(arr) > 1: 
		left_arr = arr[:len(arr)//2] # left split
		right_arr = arr[len(arr)//2:] # right split

		# recursion
		merge_sort(left_arr)
merge_sort(right_arr)

# merge
	 	i = 0 # left arr index
j = 0 # right arr index
k = 0 # merged arr index

		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i] # swap them
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		while i < len(left_arr):
			arr[k] = left_arr[i] # swap them
			j += 1
		k += 1
		
while j < len(right_arr):
			arr[k] = right_arr[j] # swap them
			j += 1
			k += 1


arr = [2, 6, 5, 1, 4, 4, 6, 8, 1]
selection_sort(arr)
print(arr) # returns 11244568

# **quicksort**
# Another divide and conquer method
# Chooses the right most value
# Then picks two indexes one just left of the most right value and one at the start
# Then it moves the one at the start and compares it to the second index. If it's greater they swap
# When the two indexes cross then you move the right most value (pivot value) in between them. 

# Basically the end is p then have two indexes. One iterates left to right looking for number smaller than p and the other moves right to left looking for a number bigger then p until they meet

21865734 # 4 is pivot 2 is index i 3 is index j
# compare 2 to 4 and leave, then 1 then 8. At 8 we swap with j

21365784 # at the point i finds a number less than 4 it stops and then j works backwards until it finds a value less than 4 

# in this case it will move past index i which is at 6

# when the indexes overlap step 1 is done and we swap i with p 

21345786

# At this point we know 4 is in the right place and numbers either side of it need sorting 

# For the two sides we do the same method as above

12345687
12345678

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition -1)
        quicksort(arr, partition + 1, right)


def partition(arr, left, right):
    i = left
    j = right -1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j: # if the crossover has happened make the swap
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

arr = [21865734]
print(quicksort(arr, 0, len(arr)-1))

'''
—————

*Big O notation and Travelling Saleman problem*

—————

Big O Notation (O stands for Order) is a way of showing how slow a function will be with increasing amounts of data
n is number of inputs being passed through function. for i in range (1000, n = 1000

o(1) = constant time. Doesn't matter how much is passed through it says the same
example is random access of element in an array or inserting at beginning

o(log n) = logarithmic time. Flattens over time
example binary search

o(n) = linear time. Straight diagonal line. Equal relationship between n and the time taken
example looping through elements in an array. Standard for i in ... is linear

o(n log n) = quasilinear time. Starts linear and then shoots up
example quicksort, merge sort (shown above)

o(n^2) = quadratic time. Exponential
example insertion sort, selection sort, bubble sort

o(n!) = factorial time. Really fast rise from start. Worst performance possible it has to check every possible combination
example travelling salesman problem

The Traveling Salesman Problem
The Traveling Salesman Problem states that you are a salesperson and you must visit a number of cities or towns.

Rules: Visit every city only once, then return back to the city you started in.
Goal: Find the shortest possible route.

There is no other way to find the shortest route than to check all possible routes.

This means that the time complexity for solving this problem is max
720 routes needs to be checked for 6 cities, 40,320 routes must be checked for 8 cities, and if you have 10 cities to visit, more than 3.6 million routes must be checked!
'''











