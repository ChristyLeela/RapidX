from mongoengine import Document
from mongoengine import IntField, StringField


class Employees(Document):
    ID = IntField(required=True, unique = True)
    emp_id = IntField()
    Name = StringField()
    Address = StringField()

    meta={'collection': 'Employees'}
