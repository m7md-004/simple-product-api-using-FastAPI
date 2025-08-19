from dataclasses import dataclass, field
from datetime import datetime
import uuid
from fastapi import FastAPI, HTTPException
from fastapi import Request,Response
import math

all_p={}

@dataclass
class Product:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    price: float = 0.0
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    def update(self, arg:dict):
        for key, value in arg.items():
            if(key=="name"):
                  self.name=value
            if(key=="description"):
                  self.description=value
            if(key=="price"):
                  self.price=value
        self.updated_at = datetime.now()

app=FastAPI()

def creat(data: dict):
    p = Product(name=data["name"],description=data["description"],price=data["price"])
    all_p[p.id] = p
    print(all_p)
    return p

    


@app.post("/products")
async def products(req:Request):
    body=await req.json()
    if not body.get("name") or not isinstance(body.get("price"), (int, float)):
            raise HTTPException(
                status_code=400,
                detail="Bad Request: 'name' is required and 'price' must be a number"
            )

    x = creat(body)
    return x.__dict__

@app.get("/products")
def products():
    return all_p

@app.put("/products/{id}")
async def update_product(id: str, req: Request):
    body = await req.json()

    # Check if product exists
    if id not in all_p:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id '{id}' not found"
        )

    # Update product
    all_p[id].update(body)
    return all_p[id]


@app.get("/products/{id}")
def getbyid(id:str):
    if id not in all_p:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id '{id}' not found"
        )
    
    return all_p[id]

@app.delete("/products/{id}")
def delete(id:str):
    if id not in all_p:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id '{id}' not found"
        )
    all_p.pop(id)
    return Response(status_code=204)