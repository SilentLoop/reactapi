# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/api/data")
def read_data():
    return {"message": "Hello from FastAPI!"}

@app.post("/api/data")
def create_item(item: Item):
    return {"name": item.name, "description": item.description}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
