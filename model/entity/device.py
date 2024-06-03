import re

from model.entity import *


class Device(Base):
    __tablename__ = "device_tbl"
    device_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)

    components = relationship("Component", back_populates="device")

    def __init__(self, device_id, name, model):
        self.device_id = device_id
        self.name = name
        self.model = model

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        if re.match("^[0-9_ \s]+$", device_id):
            self._device_id = device_id
        else:
            raise ValueError("c")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match("^[\w\sآ-ی]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام دستگاه نامعتبر است ")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if re.match("^[\w\sآ-ی]+$", model, re.I):
            self._model = model
        else:
            raise ValueError("مدل دستگاه نامعتبر است")
