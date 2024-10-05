class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)

    def __str__(self):
        employee_list = " ".join(str(hz) for hz in self.employees)
        return f"Company: {self.name}, Employees: {employee_list or 'None'}"



if __name__ == "__main__":
    company = Company("I didn't make it up")

    company.add_employee(Employee("Nick", ".2."))
    company.add_employee(Employee("Kate", ".1."))

    print(company)
