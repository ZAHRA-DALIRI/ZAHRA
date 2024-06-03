from model.bl.customer_bl import CustomerBl
from model.entity.customer import Customer
from model.tools.decorators import exception_handling


class CustomerController:
    @staticmethod
    @exception_handling
    def save(customer_id, name, family, national_code, phone_number, email, address, birth_date, status):
        customer = Customer(customer_id, name, family, national_code, phone_number, email, address, birth_date, status)
        return True, CustomerBl.save(customer)

    @staticmethod
    @exception_handling
    def edit(customer_id, name, family, national_code, phone_number, email, address, birth_date, status=True):
        customer = Customer(customer_id, name, family, national_code, phone_number, email, address, birth_date, status)
        return True, CustomerBl.edit(customer)

    @staticmethod
    @exception_handling
    def remove(customer_id):
        return True, CustomerBl.remove(customer_id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, CustomerBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(customer_id):
        return True, CustomerBl.find_by_id(customer_id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, CustomerBl.find_by_family(family)
