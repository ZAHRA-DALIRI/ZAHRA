from model.bl.component_bl import ComponentBl
from model.entity.components import Component
from model.tools.decorators import exception_handling


class ComponentController:
    @staticmethod
    @exception_handling
    def save(component_id, name, model, serial, description, device):
        component = Component(component_id, name, model, serial, description, device)
        return True, ComponentBl.save(component)

    @staticmethod
    @exception_handling
    def edit(component_id, name, model, serial, description, device):
        component = Component(component_id, name, model, serial, description, device)
        return True, ComponentBl.edit(component)

    @staticmethod
    @exception_handling
    def remove(component_id):
        return True, ComponentBl.remove(component_id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, ComponentBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(component_id):
        return True, ComponentBl.find_by_id(component_id)

    @staticmethod
    @exception_handling
    def find_by_serial(serial):
        return True, ComponentBl.find_by_serial(serial)
