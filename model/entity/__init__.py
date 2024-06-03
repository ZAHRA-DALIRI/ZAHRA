from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.entity.customer import Customer
from model.entity.employee import Employee
from model.entity.components import Component
from model.entity.device import Device
from model.entity.sell import Sell

from model.tools.validator import Validator