#error sintanxis
# if (5>2) print("It is greater")

# logical error
# result = 2+8/2
# print(f"La media es {result}")

# Exceptions
try:
    number = 10
    divider = int(input("Enter a value: "))
    result = number/divider
except ValueError:
    print("Error the value is not as expected")
except ZeroDivisionError:
    print("Error division by 0")
except Exception as e:
    print("An error has occurred: ",e)
else:
    print("As long as the except is not executed")
finally:
    print("finally")

#Raise
# raise ZeroDivisionError
# raise NameError ("exception information")

# assert(4==5)
"""
if condicion:
    raise AssertionError()

"""

# assert False, "The personalized message"