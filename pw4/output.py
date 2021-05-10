def show_Student():
    print("Student list: ")
    for Std_Info in student:
        Std_Info.show_Std()
        print(student)


def show_Course():
    print("Course list: ")
    for Course_Info in course:
        print(Course_Info.show_C())
        print(course)


def show_Mark():
    show_Student()
    s_ID = input("Select Student: ")
    for mark_Course in mark:
        if (mark_Course.s_ID == s_ID):
            mark_Course.show_M()

def show_Marks():
    print(" Here is the list of mark")
    print(mark)
    print()

def show_gpa(gpa_list):
    print("Student GPA")
    print("ID\t\tName\t\tGPA")
    for i in range(len(gpa_list)):
        gpa_list[i].display()	