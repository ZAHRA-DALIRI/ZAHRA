import re

from model.entity import *


class Customer(Base):
    __tablename__ = "customer_tbl"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    national_code = Column(String(10), unique=True, nullable=False)
    phone_number = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=True)
    status = Column(Boolean, default=True)

    sells = relationship("Sell", back_populates="customer")

    def __init__(self, customer_id, name, family, national_code, phone_number, email, address, birth_date, status=True):
        self.customer_id = customer_id
        self.name = name
        self.family = family
        self.national_code = national_code
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.birth_date = birth_date
        self.status = status

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if re.match("^[\d_\s{5}]+$", customer_id):
            self._customer_id = customer_id

        else:
            raise ValueError(" شناسه نامعتبر است ")


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if re.match("^[A-Za-zآ-ی_\-\s]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("نام نامعتبر است")


    @property
    def family(self):
        return self._family


    @family.setter
    def family(self, family):
        if re.match("^[A-Za-zآ-ی_\-\s]+$", family, re.I):
            self._family = family
        else:
            raise ValueError(" فامیلی نامعتبر است")


    @property
    def national_code(self):
        return self._national_code


    @national_code.setter
    def national_code(self, national_code):
        if re.match("^[\d{3}_\d{7}\s]+$",national_code):
            self._national_code = national_code
        else:
            raise ValueError("کد ملی نامعتبر است")


    @property
    def phone_number(self):
        return self._phone_number


    @phone_number.setter
    def phone_number(self, phone_number):
        if re.match("^[\d\+\s]+$",phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError("شماره تلفن نامعتبر است")



    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email,re.I):
            self._email= email
        else:
            raise ValueError("ایمیل نامعتبر است")


    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if re.match("^[\w\sآ-ی]+$", address, re.I):
            self._address = address
        else:
            raise ValueError("آدرس نامعتبر است ")

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        if re.match("^[\d\s_]+$", birth_date, re.I):
            self._birth_date = birth_date
        else:
            raise ValueError("تاریخ تولد نامعتبر است")



