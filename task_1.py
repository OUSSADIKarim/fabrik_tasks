def get_values (): 
    global values
    a = input("Enter the first number:")
    b = input("Enter the second number:")
    c = input("Enter the third number:")
    values = [int(a), int(b) , int(c)]

def max_value (array):
    max_value = str(max(array))
    print("The max value between " + str(array) + " is: " + max_value)

get_values()
max_value(values)