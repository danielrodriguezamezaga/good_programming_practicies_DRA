# by Daniel Rodriguez Amezaga
# 2. Make use of the filter function to build a program that, given a list of n numbers, returns those that are prime. 
# that, given a list of n numbers returns those that are prime. 
# For example, given the list [3, 4, 8, 5, 5, 5, 22, 13], the program # I implement should return [3, 4, 8, 5, 5, 22, 13]. 
# to implement must return as result [3, 5, 5, 5, 13].
import pdb
pdb.set_trace()

import math

def is_primo(num):
    """
    For a number to be prime it has to be divided twice:

       1 - divisible by 1
       2 - divisible by the same

    In the loop, we start with the two up to a number before it, so that if in the loop, we ever
    that if in the loop, if the number is ever divided, it is not prime.
    """
    if (num<=1):
        return False

    for i in range(2, math.ceil(math.sqrt(num))+1):
        if(num%i==0 and i!=num):
            return False
    return True

list = [2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10]

newList=list(filter(lambda x: is_primo(x), list))
print(newList) # [2, 3, 5, 7] # [2, 3, 5, 7] # [2, 3, 5, 7] # [2, 3, 5, 7