from controller.exceptions.exceptoins import DeviceNotFoundError
from model.da.da import DataAccess
from model.entity import Device

device_da = DataAccess(Device)


class DeviceBl:
    @staticmethod
    def save(device):
        return device_da.save(device)

    @staticmethod
    def edit(device):
        if device_da.find_by_device_id(device.device_id):
            return device_da.edit(device)
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def remove(device_id):
        device = device_da.find_by_device_id(device_id)
        if device:
            return device_da.remove(device)
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def find_all():
        device_list = device_da.find_all()
        if device_list:
            return device_list
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def find_by_id(device_id):
        device = device_da.find_by_device_id(device_id)
        if device:
            return device
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def find_by_model(model):
        device_list = device_da.find_by(Device.model == model)
        if device_list:
            return device_list
        else:
            raise DeviceNotFoundError()
