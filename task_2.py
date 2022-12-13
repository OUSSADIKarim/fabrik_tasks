import statistics 

def get_marks():
    global marks
    mark_1 = float(input("Enter your mark for Analyse module: " ))

    while mark_1 < 0 or mark_1 > 20:
        print("Error, the value you inserted is incorrect!. It should be between 0 and 20")
        mark_1 = float(input("Enter your mark for Analyse module: " ))

    mark_2 = float(input("Enter your mark for Algorithms module: " ))

    while mark_2 < 0 or mark_2 > 20:
        print("Error, the value you inserted is incorrect!. It should be between 0 and 20")
        mark_2 = float(input("Enter your mark for Algorithms module: " ))

    mark_3 = float(input("Enter your mark for Database module: " ))

    while mark_3 < 0 or mark_3 > 20:
        print("Error, the value you inserted is incorrect!. It should be between 0 and 20")
        mark_3 = float(input("Enter your mark for Database module: " ))

    marks = [mark_1, mark_2, mark_3]


def verify_min_mark(array): 
    global min_mark 
    min_mark = 5
    for mark in array:
        if mark < min_mark:
            return True

def mean(array):
    result = statistics.mean(array)

    if verify_min_mark(array) == True:
        print("You are excluded because you have marks under: " + str(min_mark))
    else:    
        if result < 10: 
            print("Your average is: " + str(result) + " . You failed.")
        elif result >= 10 and result <= 15:
            print("Your average is: " + str(result) + " . It's good.")
        elif result > 15 and result <= 20:
            print("Your average is: " + str(result) + " . It's very good.")

get_marks()
verify_min_mark(marks)
mean(marks)