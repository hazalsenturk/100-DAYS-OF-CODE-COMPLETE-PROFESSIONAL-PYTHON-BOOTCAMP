from replit import clear

#Define operations

#add
def add(n1,n2):
  return n1+n2
  
#Subtract
def subtract(n1,n2):
  return n1-n2
    
#Multiply
def multiply(n1,n2):
  return n1*n2

#Division
def divide(n1,n2):
  return n1/n2

#Define operations as a dictionary

operation_dict = { 
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}


#define function that takes inputs and calls the operatiors, returns the answer


def phyculator():
  
  num1=float(input("Enter the first number: "))
  should_continue=True
  
  while should_continue:
    
    for symbols in operation_dict:
      print(symbols)
  
    symbol=input("Pick an operation: ")
    num2=float(input("Enter the second number: "))
    
    calculation_function=operation_dict[symbol]
    answer=calculation_function(num1,num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")

    choice=input("\nType 'y' To to continue or 'n' to start a new calculation: ")
    if choice=='y':
      num1=answer
    elif choice=='n':
      should_continue=False
      clear()
      phyculator()

phyculator()