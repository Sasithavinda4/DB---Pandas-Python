#Employee class

class Employee:
    def __init__(self,id,salary,name,department):
        self.id = id
        self.salary = salary
        self.name = name
        self.department = department
        
    def increase_salary(self,percentage):
        self.salary += self.salary*percentage
        
    def update_department(self,new_department):
        self.department = new_department
        
    def display_employee_details(self):
        print("Employee ID: ",self.id,"Employee name: ",self.name,"Employee salary: ",self.salary,"Employee department: ",self.department)
        
#Employee Database class

class EmployeeDatabase:
    def __init__(self):
        self.employees = {}
        
    def add_employee(self,employee):
        if employee.id in self.employees.keys():
            print("Employee ID already exists")
            return None
        self.employees[employee.id] = employee
        
    def remove_employee(self,employee_id):
        if employee_id not in self.employees.keys():
            print("No employees for this id")
            return None
        del self.employees[employee_id]
        
    def update_employee_details(self,employee_id,new_details):
        if employee_id not in self.employees.keys():
            print("No employees for this id")
            return None
        self.employees[employee_id] = new_details
        
    def display_all_employees(self):
        for items in self.employees.values():
            items.display_employee_details()
            
#File operations
    
    def save_to_file(self,filename):
        file = open(filename,"a")
        for emp in self.employees.values():
            details = f"{emp.id},{emp.name},{emp.salary},{emp.department}\n"
            file.write(details)
            
        file.close()
        
    def load_from_file(self,filename):
        file = open(filename,"r")
        for line in file:
            id,name,salary,department = line.split()
            employee = Employee(id,name,float(salary),department)
            self.add_employee(employee)
            
        file.close()
        
#Simple menu-driven system

def main():
    
    database = EmployeeDatabase()
    print("....Welcome to the Data Base....")
    
    while True:
        print("1.Add new Employees")
        print("2.Remove employees")
        print("3.Update employee details")
        print("4.Display all employees")
        print("5.Save records to a file")
        print("6.Load recors from a file")
        print("7.Exit\n")
        
        option = int(input("....Enter Your Option...."))
        
        if(option == 1):
            id = int(input("Enter Employee ID: "))
            name = input("Enter the name: ")
            salary = float(input("Enter the salary: "))
            department = input("Enter the department: ")
            
            employee = Employee(id,name,salary,department)
            database.add_employee(employee=employee)
            
        elif(option == 2):
            id = int(input("Enter employee ID:"))
            database.remove_employee(id)
            
        elif(option == 3):
            id = int(input("Enter Employee ID: "))
            name = input("Enter the name: ")
            salary = float(input("Enter the salary: "))
            department = input("Enter the department: ")
            
            employee = Employee(id,name,salary,department)
            database.update_employee_details(id,employee)
            
        elif(option == 4):
            database.display_all_employees()
            
        elif(option == 5):
            filename = input("Enter your filename")
            database.save_to_file(filename=filename)
            
        elif(option == 6):
            filename = input("Enter your filename")
            database.load_from_file(filename=filename)
            
        elif(option == 7):
            print("Exit, Good Bye!!!!")
            break
        
        else:
            print("Invalid!!!!")
            
main()