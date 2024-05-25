from datetime import date
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


class MusicFilterContainsIgnoreCaseSchema(FilterSchema):
    song: str = Field(None, q="song__icontains")
    singer: str = Field(None, q="singer__icontains")


class MusicFilter_Gt_10_Schema(FilterSchema):
    count: Optional[int]

    def filter_count(self, val: int) -> Q:
        return Q(count__gt=val) | Q(song__icontains="test")
