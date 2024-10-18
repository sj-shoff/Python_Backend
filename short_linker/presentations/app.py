from fastapi import FastAPI, Response, status
import uvicorn
from pydantic import BaseModel


app = FastAPI()

@app.post("/health")
def hello_world() -> str:
    return "ok"


@app.get("/short")
def get_link() -> Response:
    return Response(content=None, headers={"Location": "https://misis.ru"}, status_code=status.HTTP_301_MOVED_PERMANENTLY)




