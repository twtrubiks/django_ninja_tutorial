from datetime import date
from typing import List, Optional

from ninja import Field, Schema


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return date(self.year, self.month, self.day)


class Item(Schema):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


class MultiObjFilters(Schema):
    obj__in: List[int] = Field([], alias="objs")


class OtherFilters(Schema):
    # use ... for required fields.
    owner_name: str = Field(..., alias="owner_use_name")
    lower_title: str

    @staticmethod
    def resolve_lower_title(obj: dict, context):
        # request = context["request"]
        return obj["lower_title"].lower()


class UserDetails(Schema):
    first_name: str
    last_name: str
    birthdate: date


class StatusCode(Schema):
    code: int = 200


class Token(Schema):
    token: str


class Message(Schema):
    message: str


class Error(Schema):
    error: str
