from fastapi import FastAPI, Response, status, Path
from pydantic import BaseModel
from services.short_link_service import ShortLinkService


app = FastAPI()
short_link_service = ShortLinkService()


@app.post("/health")
def hello_world() -> str:
    return "ok"

class PutLink(BaseModel):
    link: str


@app.put("/link")
def put_link(long_link: PutLink) -> PutLink:
    short_link = short_link_service.put_link(long_link.link)

    return PutLink(link=short_link)


@app.get("/short/{short_link}")
def get_link(short_link: str = Path(...)) -> Response:
    long_link = short_link_service.get_link(short_link)

    return Response(content=None, headers={"Location": "https://misis.ru"}, status_code=status.HTTP_301_MOVED_PERMANENTLY)


