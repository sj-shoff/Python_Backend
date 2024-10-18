from fastapi import FastAPI, Response, status
import uvicorn
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str

class HelloResponse(BaseModel):
    test: str


@app.post("/hello")
def hello_world(user: User) -> HelloResponse:
    return HelloResponse(test =f"Hello {user.name}!")
    

uvicorn.run(app)
