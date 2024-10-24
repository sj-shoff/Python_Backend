from fastapi import FastAPI, Response, status, Path
from pydantic import BaseModel
from services.short_link_service import ShortLinkService
import validators


app = FastAPI(
    title="Сервис генерации коротких ссылок", 
    description="Простенький сервис для создания коротких ссылок",
    )
short_link_service = ShortLinkService()


@app.post("/health")
def hello_world() -> str:
    """
    Тестовый эндпоинт
    """
    return "ok"

class PutLink(BaseModel):
    link: str


@app.put("/link")
def put_link(long_link: PutLink) -> PutLink:
    """
    Метод создания короткой ссылки по длинной ссылке
    """
    if "https://" not in long_link:
        long_link.append("https://")

    short_link = short_link_service.put_link(long_link.link)
    return PutLink(link=short_link)


@app.put("/val")
def ValidationFailure(url: PutLink) -> Response:
    """
    Валидация ссылки
    """
    if url.startswith(('http://', 'https://')):
        if not validators.url("https://misis.ru", public = True):
            return Response(
            content=None, 
            headers={"Location": "https://misis.ru"}, 
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        else:
            return Response(
                content=None, 
                headers={"Location": "https://misis.ru"}, 
                status_code=status.HTTP_200_OK
                )
    else:
        return Response(
            content=None,
            headers={"Location": "https://misis.ru"},
            status_code=status.HTTP_418_IM_A_TEAPOT
        )



@app.get("/short/{short_link}")
def get_link(short_link: str = Path(...)) -> Response:
    """
    Метод переадресации с короткой ссылки на длинную ссылку
    """
    long_link = short_link_service.get_link(short_link)

    return Response(
        content=None, 
        headers={"Location": "https://misis.ru"}, 
        status_code=status.HTTP_301_MOVED_PERMANENTLY,
        )


# url = input('Enter the url: ').lower()

# if url.startswith(('http://', 'https://')):
#     print('valid url')
# else:
#     print('invalid url')