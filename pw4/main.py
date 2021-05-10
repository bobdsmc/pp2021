def option():
    # Option: ########################################

    while (True):
        print("Select an option below: ")
        print("    +> 1. Input information about student and course")
        print("    +> 2. Input mark of student and course")
        print("    +> 3. Show information about student")
        print("    +> 4. Show information about course")
        print("    +> 5. Show mark of students in courses")
        print("    +> 6. Calculate GPA")
        print("    +> 7. Show students are sorted by GPA")
        print("    +> 0. Type '0' ('zero') to quit")

        choose = input("      => Your option: ")
        if (choose == "0"):
            break
        if (choose == "1"):
            add_Info()
        if (choose == "2"):
            marking()
        if (choose == "3"):
            show_Student()
        if (choose == "4"):
            show_Course()
        if (choose == "5"):
            show_Marks()
        if (choose == "6"):
            averageGPA()        
        else:
           print("error")