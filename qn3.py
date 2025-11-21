import csv

# Open 
with open("employees.csv", "w", newline="") as file:
 
    fieldnames = ["Name", "Department", "Salary"]  # based on Q
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    while True:
        name = input("Enter employee name (or type 'stop' to finish): ")
        if name.lower() == "stop":  # case insensitive
            break

        dept = input("Enter department: ")
        salary = input("Enter salary: ")

        #  employee data 
        writer.writerow({"Name": name, "Department": dept, "Salary": salary})

        # only if the stop implemented than csv file is written 

print("All employee data saved to employees.csv!")

# completion of program 