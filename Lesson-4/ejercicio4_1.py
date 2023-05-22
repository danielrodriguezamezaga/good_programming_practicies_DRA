# by Daniel Rodriguez Amezaga
# 1. Making use of list comprehension make a 
# program that, given a list of lists of integers, returns the maximum of each list. 
# integers, returns the maximum of each list. 
# For example, suppose the following list of lists:
# [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
# The program must return the largest element of each 
# sublist. Now, making use of the pdb, insert stop dots 
# stop points right on the line where you have implemented the # list compression. 
# list compression. Test by displaying the # contents of the variables 
# contents of the variables and continue with the line-by-line # execution. 
# execution line by line. What conclusions do you draw?
import pdb
pdb.set_trace()

list = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43,43]]
max_values = [max(sublist) for sublist in list]
print(max_values)