# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
# Derived class
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call the parent class constructor
        super().__init__(name, salary)
        self.department = department    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

# --- Dynamic input ---
print("Enter Employee details:")
emp_name = input("Enter name: ")
emp_salary = float(input("Enter salary: "))
emp = Employee(emp_name, emp_salary)
emp.display_info()
print("\nEnter Manager details:")
mgr_name = input("Enter name: ")
mgr_salary = float(input("Enter salary: "))
mgr_dept = input("Enter department: ")
mgr = Manager(mgr_name, mgr_salary, mgr_dept)
mgr.display_info()
