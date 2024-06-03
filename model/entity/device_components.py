from model.entity import *


class Component(Base):
    __tablename__ = "component_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=True)
    serial = Column(String(20), nullable=True)
    description = Column(String(100))

    device_id = Column(Integer, ForeignKey("device_tbl.device_id"))
    device = relationship("Device")

    def __init__(self, id, name, model, serial, description, device):
        self.id = id
        self.name = name
        self.model = model
        self.serial = serial
        self.description = description
        self.device = device

    # todo : getter / setter (validation)
