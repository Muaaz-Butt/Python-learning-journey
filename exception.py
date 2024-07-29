try:
  num = int(input("Enter number: "))
  print(num)
  
except Exception as e:
  print(e)
  
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
  
if num2 == 0 :
  raise ZeroDivisionError("Division by zero is not possible")
else:
  print("num1 / num2 = ", num1 / num2)
  
  
try:
  num: int = int(input("Enter number: "))
except Exception as e:
  print(e)
else:
  print("I am in else")

def main():
  try:
    num = int(input("Enter number: "))
    return
  except Exception as e:
    print(e)
    return
  finally:
    print("I am in finally")
  

main()




"""

Finally is used in functions. Even though we have called the return from the main function
but still code written in finally will run

"""