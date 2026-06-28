number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))

operator = input("Enter Operator:") 

match operator:
  case "+":
   print("Sum is", number1 + number2)
  case "-":
   print("Difference is", number1 - number2)
  case "*":
   print("Product is", number1 * number2)
  case "/":
   print("Quotient is", number1 / number2)
  case _:
   print("Enter a Valid Operator")

  
