from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


app=FastAPI()
class items(BaseModel):
    name:str
    description:str
    price:float
    tax:float

@app.post("\employees",response_model=items)
def create_item(item:items):
    return item

@app.get("\items",response_model=list[items])
def create_item():
    return [
        {"name":"samsung","description":"phone","price":34.2,"tax":23.4}
    ]



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
