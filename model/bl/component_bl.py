from controller.exceptions.exceptoins import ComponentNotFoundError
from model.da.da import DataAccess
from model.entity import Component

component_da = DataAccess(Component)


class ComponentBl:
    @staticmethod
    def save(component):
        return component_da.save(component)

    @staticmethod
    def edit(component):
        if component_da.find_by_component_id(component.component_id):
            return component_da.edit(component)
        else:
            raise ComponentNotFoundError()

    @staticmethod
    def remove(component_id):
        component = component_da.find_by_component_id(component_id)
        if component:
            return component_da.remove(component)
        else:
            raise ComponentNotFoundError()

    @staticmethod
    def find_all():
        component_list = component_da.find_all()
        if component_list:
            return component_list
        else:
            raise ComponentNotFoundError()

    @staticmethod
    def find_by_id(component_id):
        component = component_da.find_by_component_id(component_id)
        if component:
            return component
        else:
            raise ComponentNotFoundError()

    @staticmethod
    def find_by_serial(serial):
        component_list = component_da.find_by(Component.serial == serial)
        if component_list:
            return component_list
        else:
            raise ComponentNotFoundError()
