from student import Student
from csv_export import Export_CSV

login = Student.Admin_Login()

if login:

    while True:
        print("\n========== Student Management System ==========")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student By ID")
        print("4. Search Student By Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Grade System")
        print("8. Pass / Fail")
        print("9. Topper")
        print("10. Rank List")
        print("11. Average Marks")
        print("12. Statistics")
        print("13. Mark Attendance")
        print("14. View Attendance")
        print("15. Scholarship")
        print("16. Export CSV")
        print("17. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            Student.Add_Student()

        elif choice == "2":
            Student.View_Students()

        elif choice == "3":
            Student.Search_Student_ID()

        elif choice == "4":
            Student.Search_Student_Name()

        elif choice == "5":
            Student.Update_Student()

        elif choice == "6":
            Student.Delete_Student()

        elif choice == "7":
            Student.Grade_System()

        elif choice == "8":
            Student.Pass_Fail()

        elif choice == "9":
            Student.Topper()

        elif choice == "10":
            Student.Rank_List()

        elif choice == "11":
            Student.Average_Marks()

        elif choice == "12":
            Student.Statistics()

        elif choice=="13":
            Student.Mark_Attendance()

        elif choice=="14":
            Student.View_Attendance()

        elif choice=="15":
            Student.Scholarship()

        elif choice=="16":
            Export_CSV()

        elif choice=="17":
            print("Thank You.")
            break

        else:
            print("This Option Will Be Added In Next Parts.")