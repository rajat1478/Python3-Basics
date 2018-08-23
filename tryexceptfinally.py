#(i)
try:
  2+s
except TypeError:
  print "Therer was a TypeError!"
finally:
  print "Finally this was printed"
  
#(ii)
try: 
  f = open('testfile1234','w')
  f.write('Test write this')
except:
  print 'Error in writing to this file'
else:
  print 'File write was a success'

#(iii)
try: 
  f = open('testfile1234','w')
  f.write('Test write this')
except:
  print 'There was an error'
finally:
  print 'Always execute finally code blocks'
