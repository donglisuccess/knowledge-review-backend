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
    
@app.get("/api/getUserInfo")
def getUserInfo():
    return {
        "code": 0,
        "data": {
            # mock数据
            "name": "dongli",
            "age": 18,
            "gender": "男",
            "address": "北京市朝阳区",
            "phone": "13800138000",
            "email": "zhangsan@example.com",
            "avatar": "https://example.com/avatar.jpg",
            "status": "在线",
            "lastLoginTime": "2021-01-01 12:00:00"
        }
    }
    