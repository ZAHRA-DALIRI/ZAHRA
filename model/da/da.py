from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base

connection_string = "mysql+pymysql://root:zahra1379@localhost:3306/bread"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class DataAccess:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        return entity

    def remove(self, entity):
        session.delete(entity)
        session.commit()
        return entity

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        return entity_list

    def find_by(self, find_statement):
        entity = session.query(self.class_name).filter(find_statement).all()
        return entity

    def find_by_employee_id(self, employee_id):
        entity = session.get(self.class_name, employee_id)
        return entity

    def find_by_customer_id(self, customer_id):
        entity = session.get(self.class_name, customer_id)
        return entity

    def find_by_device_id(self, device_id):
        entity = session.get(self.class_name, device_id)
        return entity

    def find_by_component_id(self, component_id):
        entity = session.get(self.class_name, component_id)
        return entity

    def national_code(self, national_code):
        entity = session.get(self.class_name, national_code)
        return entity
