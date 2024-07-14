from datetime import date, datetime
from typing import List, Optional

from django.db.models import Q
from ninja import Field, FilterSchema, ModelSchema, Schema

from .models import Music, Sheet


class SheetSchema(ModelSchema):
    class Meta:
        model = Sheet
        fields = [
            "id",
            "name",
        ]


class SheetIn(Schema):
    name: str


class MusicSchema(ModelSchema):
    sheet: Optional[SheetSchema] = None
    sheet_name: Optional[str] = None

    class Meta:
        model = Music
        fields = [
            "id",
            "song",
            "singer",
            "count",
            "last_modify_date",
            "created",
        ]

    @staticmethod
    def resolve_sheet_name(obj: Music):
        return obj.sheet.name.upper()


class CreateMusicSchema(Schema):
    song: str
    singer: str
    count: int = 0


class MusicIn(Schema):
    song: str
    singer: str
    count: int = 0
    sheet: Optional[int] = None

    class Config:
        extra = "forbid"


class MusicOut(Schema):
    id: int
    song: str
    singer: str
    count: int = 0
    last_modify_date: datetime
    sheet: Optional[SheetSchema] = None


class MultiMusicFilters(Schema):
    music_ids: List[int] = Field([], alias="musics")


class MusicFilterSchema(FilterSchema):
    song: str  # 預設會考慮大小寫
    singer: Optional[str] = None
    last_modify_date: Optional[date] = None
    # sheet: Optional[str] = Field(None, q="sheet", ignore_none=False)

    def filter_last_modify_date(self, val: date) -> Q:
        return Q(last_modify_date__date=val)


class MusicCustomExpressionFilterSchema(FilterSchema):
    song: Optional[str] = None
    singer: Optional[str] = None
    last_modify_date: Optional[date] = None
    sheet_name: Optional[str] = None
    operator: str | None = "and"

    # https://django-ninja.dev/guides/input/filtering/
    # The custom_expression method takes precedence over any other definitions described earlier,
    # including filter_<fieldname> methods.

    def custom_expression(self) -> Q:
        q = Q()
        if self.operator == "and":
            if self.song:
                q &= Q(song__icontains=self.song)
            if self.singer:
                q &= Q(singer__icontains=self.singer)
            if self.last_modify_date:
                q &= Q(last_modify_date__date=self.last_modify_date)
            if self.sheet_name:
                q &= Q(sheet__name__icontains=self.sheet_name)
        else:
            if self.song:
                q |= Q(song__icontains=self.song)
            if self.singer:
                q |= Q(singer__icontains=self.singer)
            if self.last_modify_date:
                q |= Q(last_modify_date__date=self.last_modify_date)
            if self.sheet_name:
                q |= Q(sheet__name__icontains=self.sheet_name)
        return q


def apply_song(q, song, operator_func):
    if song:
        q = operator_func(q, Q(song__icontains=song))
    return q


def apply_singer(q, singer, operator_func):
    if singer:
        q = operator_func(q, Q(singer__icontains=singer))
    return q


def apply_last_modify_date(q, last_modify_date, operator_func):
    if last_modify_date:
        q = operator_func(q, Q(last_modify_date__date=last_modify_date))
    return q


def apply_sheet_name(q, sheet_name, operator_func):
    if sheet_name:
        q = operator_func(q, Q(sheet__name__icontains=sheet_name))
    return q


class MusicCustomExpressionRefactorFilterSchema(FilterSchema):
    song: Optional[str] = None
    singer: Optional[str] = None
    last_modify_date: Optional[date] = None
    sheet_name: Optional[str] = None
    operator: str | None = "and"

    def custom_expression(self) -> Q:
        q = Q()
        operator = Q.__and__ if self.operator == "and" else Q.__or__
        q = apply_song(q, self.song, operator)
        q = apply_singer(q, self.singer, operator)
        q = apply_last_modify_date(q, self.last_modify_date, operator)
        q = apply_sheet_name(q, self.sheet_name, operator)
        return q


class MusicFilterContainsIgnoreCaseSchema(FilterSchema):
    song: str = Field(None, q="song__icontains")
    singer: str = Field(None, q="singer__icontains")


class MusicFilter_Gt_10_Schema(FilterSchema):
    count: Optional[int]

    def filter_count(self, val: int) -> Q:
        return Q(count__gt=val) | Q(song__icontains="test")
