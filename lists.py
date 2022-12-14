nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_check = input("Enter the num to check: \n")

while not num_check.isdigit():
    num_check = input("Error, please enter a valid number.\nEnter the num to check: \n")

def num_checker(number) :
    if float(number) in nums:
        print("The num " + str(number) + " exists in nums")
    else:
        print("The num " + str(number) + " doesn't exist in nums")
    

num_checker(num_check)

