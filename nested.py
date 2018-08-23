#(i)local
f = lambda x: x**2

#(ii)enclosing fuction locals

name = 'This is global name'

def greet():
  #enclosing function
  name = 'Speedy'
  
  def hello():
    print'Hello'+name
    
  hello()
greet()

#(iii)Built-in
len(s)

#(iv)local veriable
x =50
def func():
  print 'x is', x
  x = 2
  print 'changed local x to', x
func(x)
print 'x is still', x

#(v)Global statement
x = 50
def func():
  global x
  print 'This fuction is now using the global x!'
  print 'Because of global x is:', x
  x=2
  print 'Ran func(), changed global x to:',x
print 'Before calling func() x is:',x
func()
print 'Value of x(outside of func()) is:'x
