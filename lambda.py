#(i)making a square fuction
square = lambda num: num**2
square(10)

#(ii)checking if number is even
even = lambda num: num%2 == 0
even(4)
even(7)

#(iii)grab the first number of string
first = lambda s: s[0]
first('Hello')

#(iv)reversing the string
rev = lambda s: s[::-1]
rev('Hello')

#(v) adder
adder = lambda x,y :x+y
adder(15,16)

#(vi) checking the length
len_check = lambda s : len(s)
len_check('hello')
