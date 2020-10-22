class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

''' 
        OUTPUT:
This Polo is made of Cotton

'''
print('---------------------------------------------------------------------')


class Animal:
  sound = ""
  def __init__(self,name):
    self.name = name
  def speak(self):
    print("{sound} I'm {name}! {sound}".format(name = self.name,sound  = self.sound))
    
class Piglet(Animal):
  sound = "Oink!"
class Cow(Animal):
  sound = "Mooooo!"
 
hamlet = Piglet("Hamlet")
hamlet.speak()

milky = Cow("Milky White")
milky.speak()
