class Animal:
  def __init__(self):
    print "Animal Created"
    
  def whoAmI(self):
    print "Animal"
    
  def est(self):
    print "Eating"
    
class Dog(Animal)
  def __init__(self):
    Animal.__init__(self)
    print "Dog Created"
    
  def whoAmI(self):
    print "Dog"
    
  def bark(self):
    print "Woof!"
    
 d = Dog()
 
 d.whoAmI()
 
 d.eat()
 
 d.bark()
