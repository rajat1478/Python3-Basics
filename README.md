# Python3-Basics
Python was developed by Guido van Rossum in early 1990’s and its latest version is 3.6, we can simply call it as Python3. Python 3.0 was released in 2008.
## Print
In python3 t print any line we use 'print("<text>")'.
## Variables
n other programming languages like C, C++ and Java, you will need to declare the type of variables but in Python you don’t need to do that. Just type in the variable and when values will be given to it, then it will automatically know whether the value given would be a int, float or char or even a String.
## Listing
  List is the most basic Data Structure in python. List is mutable data structure it means items can be added to list later after the list creation. Its like you are going to shop at local market and made a list of some items and later on you can add more and more items to the list.append() function is used to add data to the list.
## Input/Output
  input() function is used to take input from the user.
  print() functiom is used to give output.
## Selection
  In python selection is made using 'if' and 'elif'(here we use elif on the place of elseif).
## Functions
  you can think of functions like a bunch of code that is intended to do a particular task in the whole Python script. Python   used the keyword ‘def’ to define a function.
## For loop
  For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. The difference between range and   xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an           iterator, which is more efficient.
## While loop
  While loop repeat as long as a certain bollean condition is met.The while loop is to perform iteration. A while statement repeatedly execute a single statement untill a true value occure.
```
  while test:
      code statement
  else:
      final code statements
```
## Assignment Statement
    You’ll store values in variables with an assignment statement. An assignment statement consists of a variable name, an         equal sign (called the assignment operator), and the value to be stored.
## Break/Continue
  break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the       "for" or "while" statement.
## Modules
  Python has a very rich module library that has several functions to do many tasks. 'import’ keyword is used to import a       particular module into your python code. 
## Binary Operations
```  
  Operator      Operation                           Example
  **            Exponent                            2 ** 2 = 8
  %             Modules/remainder                   22 % 8= 6
  //            Integer division/floored quotient   22 //8 = 2
  /             Division                            22 / 8 = 2.75
  *             Multiplication                      2 * 5 = 10
  -             Subtraction                         5 - 3 = 2
  +             Addition                            7 + 3 = 10
```
## Conditional Statements
  If the condition "condition_1" is True, the statements in the block statement_block_1 will be executed. If not, condition_2   will be executed. If condition_2 evaluates to True, statement_block_2 will be executed, if condition_2 is False, the   statements in statement_block_3 will be executed.
```
  if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
## Range
  range() allow us to create a list of numbers ranging from a starting point up to an ending point . We can also specifi step size.
## Comparison Operators
  These operator will allow us to compare variables and output a boolean value.
## Chained Comparison Operators
  An interestion feature of Pyton is the ability to chain multiple comperision to perform a more complex test. You can use these chained compariso as a shorthand for large boolean expression.
## Methods
  Methods are essentially fuction built into objects. Methods will perform specifi actions on the object and can also take arguments, just like a fuction.
```
  object.methods(arg1,arg2,etc....)
```
  * Append
  * Count
  * Extend
  * insert
  * pop
  * remove
  * reverse
  * sort
## Lambda Fuction
  Lambda fuction allow us to create "anonymos" fuctions.This basically mean we can quickly make ad-hoc fuction without needing to properly define a fuction using def. Fuction object return by running lambda expression work exectely the same as those created and assigned by defs.
```
  <function__main__.<lambda>>
```
  Lambda expression really shine when used in conjuction with map(),filter() and redce().
## Nested Statements and Scope
  When you create a veriable name in Python the name is store in namespace. Veriable name also have a scope, the scope determines the visbility of that veriable name to other parts of your code.
  Name assignment will create and change local name by default.Name references at most four scope:
  
  *Local 
  *Enclosing fuction 
  *Global 
  *Built-in
  
  ### Local
  Name assigned in any way in fuction, and not declared in global in that function.
  ### Enclosing fuction locals 
  Name in the local scope of any amd all enclosing fuction, from inner to outer.
  ### Global
  Name assigned at the top-level of a module file, or declared global in a def within the file.
  ### Built-in 
  Name preassigned in the built-in name module : open, range, syntex....
  
## Modules & Packages
  This import a module into your current work-place. It's important that you have to either tell Python what function you want to import, or state the module you are importing from. To download newmodule:
```
for anaconda
conda install *module name*
pip install *module name*(optional)
```
## Errors
 Syntax errors, also known as parsing errors.The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. The error is caused by (or at least detected at) the token preceding the arrow, the error could be detected at the function print(), since a colon (':') is missing before it and etc. File name and line number are printed so you know where to look in case the input came from a script.
## Exceptions
 If a statement or expressions is syntectically correct, it may cause an error when an attempt is made to execute it. Error detected during execution is called Exceptions.
