from django.http import HttpResponse
from ninja import File, Form, Path, Query, Router
from ninja.files import UploadedFile

from utils.exception import ServiceUnavailableError

from .schemas import (
    Error,
    Item,
    Message,
    MultiObjFilters,
    OtherFilters,
    PathDate,
    StatusCode,
    Token,
    UserDetails,
)

router = Router(tags=["example"])


@router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@router.get("/date_1/{year}/{month}/{day}")
def date_1(request, year: int, month: int, day: int):
    return {"date": [year, month, day]}


@router.get("/date_2/{year}/{month}/{day}")
def date_2(request, content: Path[PathDate]):
    return {"date": content.value()}


@router.get("/data")
def list_data(request, limit: int, offset: int = 0):
    data = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]

    return data[offset : offset + limit]


@router.post("/items")
def create_obj(request, item: Item):
    return item


@router.get("/items/{item_id}")
def get_item(request, item_id: int, q: str):
    return {"item_id": item_id, "q": q}


@router.get("/multi_obj")
def test_multi_obj(request, filters: Query[MultiObjFilters]):
    return filters.dict()


@router.get("/other_filters")
def test_other_filters(request, filters: Query[OtherFilters]):
    return filters.dict()


@router.get("/django_http_response")
def result_django(request):
    return HttpResponse("some data")


@router.post("/login")
def login(request, username: Form[str], password: Form[str]):
    return {"username": username, "password": "*****"}


@router.post("/users")
def create_user(request, details: Form[UserDetails]):
    return [details.dict()]


@router.post("/upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    return {"name": file.name, "len": len(data)}


@router.get("/test_service_unavailable_error")
def test_service_unavailable_error(request):
    raise ServiceUnavailableError


@router.post(
    "/test_response_code", response={200: Token, 204: None, 401: Message, 400: Error}
)
def test_response_code(request, status_code: StatusCode):
    if status_code.code == 200:
        return 200, {"token": "xxxxx123"}
    if status_code.code == 204:
        return 204, None
    if status_code.code == 401:
        return 401, {"message": "Unauthorized"}

    return 400, {"error": "請輸入正確狀態碼"}
