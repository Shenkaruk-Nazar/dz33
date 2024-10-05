class Employee:
    def __init__(self, name, work):
        self.name = name
        self.work = work

    def __str__(self):
        return f"{self.name} - {self.work}"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        print(f"Departament {self.name}:")
        for employee in self.employees:
            print(employee)


# Приклад використання
if __name__ == "__main__":
    hz_department = Department("Hz")
    hz_department.add_employee(Employee("Employee 1", ".1."))
    hz_department.add_employee(Employee("Employee 2", ".2."))
    hz_department.list_employees()
