from controller.exceptions.exceptoins import CustomerNotFoundError
from model.da.da import DataAccess
from model.entity import Customer

customer_da = DataAccess(Customer)


class CustomerBl:
    @staticmethod
    def save(customer):
        return customer_da.save(customer)

    @staticmethod
    def edit(customer):
        if customer_da.find_by_customer_id(customer.customer_id):
            return customer_da.edit(customer)
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def remove(customer_id):
        customer = customer_da.find_by_customer_id(customer_id)
        if customer:
            return customer_da.remove(customer)
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_all():
        customer_list = customer_da.find_all()
        if customer_list:
            return customer_list
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_by_id(customer_id):
        customer = customer_da.find_by_customer_id(customer_id)
        if customer:
            return customer
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_by_family(family):
        customer_list = customer_da.find_by(Customer.family == family)
        if customer_list:
            return customer_list
        else:
            raise CustomerNotFoundError()
