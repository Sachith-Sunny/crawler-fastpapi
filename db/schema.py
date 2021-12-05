from pydantic import BaseModel

class NewData(BaseModel):
    manufacturer : str
    category : str
    model : str
    part : str
    part_category : str


