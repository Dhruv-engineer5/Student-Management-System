import os

class Student:
    # ---------------- ADMIN LOGIN ----------------
    @staticmethod
    def Admin_Login():
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        try:
            with open("Admin.txt", "r") as file:
                admin = file.readline().strip().split(",")
                if username == admin[0] and password == admin[1]:
                    print("\nLogin Successful\n")
                    return True
                else:
                    print("\nInvalid Username or Password\n")
                    return False
        except FileNotFoundError:
            print("Admin File Not Found.")
            return False

    # ---------------- ADD STUDENT ----------------
    @staticmethod
    def Add_Student():
        student_id = input("Student ID : ")
        name = input("Student Name : ")
        email = input("Email : ")
        mobile = input("Mobile : ")
        age = input("Age : ")
        course = input("Course : ")
        marks = input("Marks : ")
        admission = input("Admission Date (DD-MM-YYYY) : ")
        with open("Students.txt", "a") as file:
            file.write(
                f"{student_id},{name},{age},{course},{marks},{admission},{email},{mobile}\n"
                )
        print("\nStudent Added Successfully.\n")

    # ---------------- VIEW STUDENTS ----------------
    @staticmethod
    def View_Students():
        try:
            with open("Students.txt", "r") as file:
                found = False
                for line in file:
                    if line.strip() == "":
                        continue
                    student = line.strip().split(",")
                    print("-" * 40)
                    print("Student ID     :", student[0])
                    print("Name           :", student[1])
                    print("Age            :", student[2])
                    print("Course         :", student[3])
                    print("Marks          :", student[4])
                    print("Admission Date :", student[5])
                    print("Email          :", student[6])
                    print("Mobile         :", student[7])
                    found = True
                if not found:
                    print("No Student Found.")
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- SEARCH STUDENT BY ID ----------------
    @staticmethod
    def Search_Student_ID():
        search_id = input("Enter Student ID : ")
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    if student[0] == search_id:
                        print("\nStudent Found\n")
                        print("Student ID     :", student[0])
                        print("Name           :", student[1])
                        print("Age            :", student[2])
                        print("Course         :", student[3])
                        print("Marks          :", student[4])
                        print("Admission Date :", student[5])
                        return
                print("\nStudent Not Found.")
        except FileNotFoundError:
            print("Students.txt File Not Found.")

        # ---------------- SEARCH STUDENT BY NAME ----------------
    @staticmethod
    def Search_Student_Name():
        search_name = input("Enter Student Name : ").lower()
        found = False
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    if student[1].lower() == search_name:
                        print("\nStudent Found\n")
                        print("Student ID     :", student[0])
                        print("Name           :", student[1])
                        print("Age            :", student[2])
                        print("Course         :", student[3])
                        print("Marks          :", student[4])
                        print("Admission Date :", student[5])
                        found = True
            if not found:
                print("\nStudent Not Found.")
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- UPDATE STUDENT ----------------
    @staticmethod
    def Update_Student():
        search_id = input("Enter Student ID To Update : ")
        students = []
        updated = False
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    if student[0] == search_id:
                        print("\nStudent Found\n")
                        student[1] = input("New Name : ")
                        student[2] = input("New Age : ")
                        student[3] = input("New Course : ")
                        student[4] = input("New Marks : ")
                        student[5] = input("New Admission Date : ")
                        updated = True
                    students.append(",".join(student))
            with open("Students.txt", "w") as file:
                for student in students:
                    file.write(student + "\n")
            if updated:
                print("\nStudent Updated Successfully.")
            else:
                print("\nStudent Not Found.")
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- DELETE STUDENT ----------------
    @staticmethod
    def Delete_Student():
        search_id = input("Enter Student ID To Delete : ")
        students = []
        deleted = False
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    if student[0] != search_id:
                        students.append(",".join(student))
                    else:
                        deleted = True
            with open("Students.txt", "w") as file:
                for student in students:
                    file.write(student + "\n")
            if deleted:
                print("\nStudent Deleted Successfully.")
            else:
                print("\nStudent Not Found.")
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- TOPPER ----------------
    @staticmethod
    def Topper():
        topper = None
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    student[4] = int(student[4])
                    if topper is None or student[4] > topper[4]:
                        topper = student
            if topper:
                print("\n========== TOPPER ==========")
                print("Student ID :", topper[0])
                print("Name       :", topper[1])
                print("Course     :", topper[3])
                print("Marks      :", topper[4])
            else:
                print("No Students Found.")
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- GRADE SYSTEM ----------------
    @staticmethod
    def Grade_System():
        try:
            with open("Students.txt", "r") as file:
                print("\n========== GRADES ==========\n")
                for line in file:
                    student = line.strip().split(",")
                    marks = int(student[4])
                    if marks >= 91:
                        grade = "A+"
                    elif marks >= 81:
                        grade = "A"
                    elif marks >= 71:
                        grade = "B"
                    elif marks >= 61:
                        grade = "C"
                    elif marks >= 41:
                        grade = "D"
                    else:
                        grade = "F"
                    print(student[1], "=", grade)
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- PASS FAIL ----------------
    @staticmethod
    def Pass_Fail():
        try:
            with open("Students.txt", "r") as file:
                print("\n========== RESULT ==========\n")
                for line in file:
                    student = line.strip().split(",")
                    marks = int(student[4])
                    if marks >= 35:
                        result = "PASS"
                    else:
                        result = "FAIL"
                    print(student[1], "=", result)
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- RANK LIST ----------------
    @staticmethod
    def Rank_List():
        students = []
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    student[4] = int(student[4])
                    students.append(student)
            students.sort(key=lambda x: x[4], reverse=True)
            print("\n========== RANK LIST ==========\n")
            rank = 1
            for student in students:
                print(rank, ".", student[1], "-", student[4])
                rank += 1
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- STATISTICS ----------------
    @staticmethod
    def Statistics():
        total = 0
        highest = -1
        lowest = 101
        total_marks = 0
        pass_students = 0
        fail_students = 0
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    marks = int(student[4])
                    total += 1
                    total_marks += marks
                    if marks > highest:
                        highest = marks
                    if marks < lowest:
                        lowest = marks
                    if marks >= 35:
                        pass_students += 1
                    else:
                        fail_students += 1
            if total == 0:
                print("No Students Found.")
                return
            average = total_marks / total
            print("\n========== STATISTICS ==========\n")
            print("Total Students :", total)
            print("Average Marks  :", round(average, 2))
            print("Highest Marks  :", highest)
            print("Lowest Marks   :", lowest)
            print("Pass Students  :", pass_students)
            print("Fail Students  :", fail_students)
        except FileNotFoundError:
            print("Students.txt File Not Found.")

    # ---------------- AVERAGE MARKS ----------------
    @staticmethod
    def Average_Marks():
        total = 0
        marks_sum = 0
        try:
            with open("Students.txt", "r") as file:
                for line in file:
                    student = line.strip().split(",")
                    marks_sum += int(student[4])
                    total += 1
            if total == 0:
                print("No Students Found.")
                return
            print("Average Marks :", round(marks_sum / total, 2))
        except FileNotFoundError:
            print("Students.txt File Not Found.")


    # ---------------- MARK ATTENDANCE ----------------
    @staticmethod
    def Mark_Attendance():
        student_id = input("Enter Student ID : ")
        date = input("Enter Date (DD-MM-YYYY) : ")
        status = input("Present / Absent : ")
        with open("Attendance.txt", "a") as file:
            file.write(f"{student_id},{date},{status}\n")
        print("Attendance Saved Successfully.")

    # ---------------- VIEW ATTENDANCE ----------------
    @staticmethod
    def View_Attendance():
        try:
            with open("Attendance.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    print("-"*35)
                    print("Student ID :", data[0])
                    print("Date       :", data[1])
                    print("Status     :", data[2])
        except FileNotFoundError:
            print("Attendance File Not Found.")

    # ---------------- SCHOLARSHIP ----------------
    @staticmethod
    def Scholarship():
        try:
            with open("Students.txt","r") as file:
                print("\nScholarship Eligible Students\n")
                for line in file:
                    student = line.strip().split(",")
                    marks = int(student[4])
                    if marks >= 85:
                        print(student[1], "-", marks)
        except FileNotFoundError:
            print("Students.txt File Not Found.")