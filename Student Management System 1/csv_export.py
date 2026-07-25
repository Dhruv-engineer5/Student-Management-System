import csv

def Export_CSV():
    with open("Students.txt","r") as file:
        rows=[]
        for line in file:
            rows.append(line.strip().split(","))
    with open("Student_Report.csv","w",newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([
            "Student ID",
            "Name",
            "Age",
            "Course",
            "Marks",
            "Admission Date",
            "Email",
            "Mobile"
        ])
        writer.writerows(rows)
    print("CSV Exported Successfully.")