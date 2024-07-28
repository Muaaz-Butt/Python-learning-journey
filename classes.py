class Employee:
  language = "py"
  salary = 12000
  
  #self parameter
  def getInfo(self) :
    print(f"Language is: {self.language}\nSalary is: {self.salary}")
    
  @staticmethod
  def greet() :
    print("Good morning")
    
  # Constructor
  def __init__(self) :              #Dunder method which is automatically called
    print("I am creating an object")
  
  def __init__ (self, name, language, salary) :
    self.name = name
    self.language= language
    self.salary= salary
    
    
    
  
#Muaaz = Employee()
#Muaaz.name = "Muaaz Butt"

#Zayyad = Employee()

Hammad = Employee("Hammad Butt", "cpp", 130000)

Hammad.getInfo()

#print(Muaaz.name, Muaaz.language, Muaaz.salary)

#Zayyad.getInfo()

"""

Here name is object attribute and language and salary are class attributes as they directly belong to the class


"""