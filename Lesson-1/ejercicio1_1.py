# Author: Daniel Rodriguez Amezaga

class MiException(Exception):
    def __init__(self, params):
        self.params = params
          
try:
    numero = int(input("Enter a value: "))
    raise MiException(numero) 
 
except ValueError:
    print("The value entered is not an integer")
    
except MiException as e:
    if e.params > 20:
        print("The value entered is greater than 20")
    else:
        print(e.params)





