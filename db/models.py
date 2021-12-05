from mongoengine import Document
from mongoengine.fields import StringField


class Data(Document):
    manufacturer = StringField()
    category = StringField()    
    model = StringField()
    part = StringField()
    part_category = StringField()