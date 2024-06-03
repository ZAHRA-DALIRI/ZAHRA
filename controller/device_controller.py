from model.bl.device_bl import DeviceBl
from model.entity.device import Device
from model.tools.decorators import exception_handling


class DeviceController:
    @staticmethod
    @exception_handling
    def save(device_id, name, model):
        device = Device(device_id, name, model)
        return True, DeviceBl.save(device)

    @staticmethod
    @exception_handling
    def edit(device_id, name, model):
        device = Device(device_id, name, model)
        return True, DeviceBl.edit(device)

    @staticmethod
    @exception_handling
    def remove(device_id):
        return True, DeviceBl.remove(device_id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, DeviceBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(device_id):
        return True, DeviceBl.find_by_id(device_id)

    @staticmethod
    @exception_handling
    def find_by_model(model):
        return True, DeviceBl.find_by_model(model)
