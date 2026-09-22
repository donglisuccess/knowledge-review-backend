from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoRequest(BaseModel):
    name: str
    
@app.get("/api/hello")
def hello():
    return {
        "code": 0,
        "message": "hello from python backend"
    }
    
  
@app.post("/api/echo")
def echo(request: EchoRequest):
    return {
        "code": 0,
        "data": {
            "name": request.name
        }
    }