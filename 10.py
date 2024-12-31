class Person:
    """
    A class to represent a person with a name and an age.

    :param name: The name of the person.
    :type name: str
    :param age: The age of the person.
    :type age: int
    """

    def __init__(self, name, age):
        """
        Initialize a Person object with name and age.

        :param name: The name of the person.
        :type name: str
        :param age: The age of the person.
        :type age: int
        """
        self.name = name
        self.age = age

    def display_details(self):
        """
        Display the details of the person (name and age).

        :return: None
        :rtype: None
        """
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    """
    A class to represent an employee, inheriting from Person, with an additional salary attribute.

    :param name: The name of the employee.
    :type name: str
    :param age: The age of the employee.
    :type age: int
    :param salary: The salary of the employee.
    :type salary: float
    """

    def __init__(self, name, age, salary):
        """
        Initialize an Employee object with name, age, and salary.

        :param name: The name of the employee.
        :type name: str
        :param age: The age of the employee.
        :type age: int
        :param salary: The salary of the employee.
        :type salary: float
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """
        Display the details of the employee (name, age, and salary).

        :return: None
        :rtype: None
        """
        super().display_details()
        print(f"Salary: {self.salary}")
