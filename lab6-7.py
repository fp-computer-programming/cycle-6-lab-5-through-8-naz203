num1= int (input ("enter number 1:"))
num2= int (input("enter number :2"))
num3= int (input ("Enter number 3: "))
# Construct a List of the 3 input values in the order that the user gave then 
num_list = [num1, num2, num3]
9
50
11
#Display a list with each of the values as integers that have been doubled 
doubled_list = [num*2 for num in num_list] 
print (doubled_list)
