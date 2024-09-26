def add_Info():
    # Input Student information ##############################
    # Contain:
    #     - ID
    #     - Name
    #     - Date of Birth
    s_Num = int(input("How many students?\n  -> There are: "))
    for i in range(s_Num):
        Std_Info.s_ID = input("      - Student " + str(i + 1) + " ID: ")
        Std_Info.s_Name = input("      - Student " + str(i + 1) + " Name: ")
        Std_Info.s_DoB = ("      - Student " + str(i + 1) + " DoB: ")
        student.append(
            {"Student " + str(i + 1) + " Id": Std_Info.s_ID, "Student " + str(i + 1) + " Name": Std_Info.s_Name,
             "Student " + str(i + 1) + " DoB": Std_Info.s_DoB})
        print()
        print("-----------------------------------------------------------------")

    # Input Course information ###############################
    # Contain:
    #      - ID
    #      - Name
    c_Num = int(input("How many courses?\n  -> There are: "))
    for i in range(c_Num):
        print("    * Enter information about course " + str(i + 1) + ": ")
        c_ID = input("      - Course " + str(i + 1) + " ID: ")
        c_Name = input("      - Course " + str(i + 1) + " Name: ")
        course.append({"Course " + str(i + 1) + "Id": c_ID, "Course " + str(i + 1) + "Name": c_Name})
        print()
        print("-----------------------------------------------------------------")

def averageGPA():
    sum_credit = 0
    total_mark = 0
    for i in range(len(student)):
        for j in range(len(course)):
            total_mark += mark[i][j].get_mark * course[j].get_credit
            sum_credit = course[j].get_credit
    averageGPA = math.floor((total_mark/sum_credit * 10)/10)
    return averageGPA

def marking():
    print("-------------------------------")
    print()

    # Input for choosing:
    #      - Student:      ###########################
    show_Student()
    print(" => Select student by ID:")
    s_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    #      - Course:       ###########################
    show_Course()
    print(" => Select course by ID:")
    c_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    # Mark #######################################
    print()
    m = input(" => Enter the mark: ")
    mark.append({"Student ID": s_ID, "Course ID": c_ID, "Mark": m})
    print()