##Different Instances are Different Objects
#Let's make three dogs

class Dog: 
	pass
fido = Dog()
fido

# <__main__.Dog object at 0x1049a87f0>

snoopy = Dog()
snoopy
#<__main__.Dog object at 0x1049271d90>


lassie = Dog()
lassie
#<--main__.Dog object at 0x10498c040>


#Notice that every time you make an instance of class. Python  tells  you that the return value is something that looks like # <__main__.Dog object at 0x1049a87f0>. This is the default way that Python communicates to you that you are dealing with an instance of a particular class. The  __main__ tells you that the object is accessible from a global scope in the current modile (file or shell) that you are working in. 0x1049a87f0 describes the instance's location in memory.

class Dog: 
	pass

fido = Dog()
fido
# <__main __.Dog object at 0x104971d90>

snoopy == fido
#false


#Classes are the bluebring that define the behavior and  information our objects will contain. They let us manufacture and instantiate new instances.

#Conslusion - in summary : to create a new class defintion . use the  class keyword. A class is like a template, or a blue print, for vreating objects with similar  characteristics. 
# To use the class to create individual objects, call the class with closed parenthesis as you would a function or method. THis will instantiate(create a new instance of) an object from the class. Each instance created will be a unique object in menoty.

