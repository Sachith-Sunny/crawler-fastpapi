import json
from fastapi import FastAPI
from db.models import Data
from mongoengine import connect
from typing import Optional
from db.schema import NewData
from mongoengine.queryset.visitor import Q
from scrapper.scrape import scrape_now

app = FastAPI()
connect(db="pytest",host = "localhost",port = 27017)

@app.get("/")
def home():
    return {"message": "it works"}


# @app.post("/", response_description="Add new student", response_model=StudentModel)
# async def create_entry(student: StudentModel = Body(...)):
#     student = jsonable_encoder(student)
#     new_student = await db["students"].insert_one(student)
#     created_student = await db["students"].find_one({"_id": new_student.inserted_id})
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)
    
@app.get("/all")
def getall():
    data = Data.objects()    
    print(data)

@app.post("/add")
def add(newdata : NewData):
    new_record = Data(manufacturer = newdata.manufacturer,category = newdata.category,model = newdata.model,part = newdata.part,part_category = newdata.part_category)
    new_record.save()
    return {"message": "Success"}    


@app.get("/search")
def search(manufacturer: Optional[str] = None):
    result = json.loads(Data.objects.filter(manufacturer = manufacturer).to_json())   
    print(result)
    return {"result":result}

@app.get("/search2")
def search2(part_category: Optional[str] = None):
    result = json.loads(Data.objects.filter(part_category = part_category).to_json())   
    print(result)
    return {"result":result}
@app.post("/scrape")
def scrape():
    scrape_now()
