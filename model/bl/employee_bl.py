from controller.exceptions.exceptoins import EmployeeNotFoundError
from model.da.da import DataAccess
from model.entity import Employee

employee_da = DataAccess(Employee)


class EmployeeBl:
    @staticmethod
    def save(employee):
        return employee_da.save(employee)

    @staticmethod
    def edit(employee):
        if employee_da.find_by_employee_id(employee.employee_id):
            return employee_da.edit(employee)
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def remove(employee_id):
        employee = employee_da.find_by_employee_id(employee_id)
        if employee:
            return employee_da.remove(employee)
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_all():
        employee_list = employee_da.find_all()
        if employee_list:
            return employee_list
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_by_id(employee_id):
        employee = employee_da.find_by_employee_id(employee_id)
        if employee:
            return employee
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_by_family(family):
        employee_list = employee_da.find_by(Employee.family == family)
        if employee_list:
            return employee_list
        else:
            raise EmployeeNotFoundError()
