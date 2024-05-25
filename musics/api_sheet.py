from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from musics.models import Sheet

from .schemas import (
    SheetIn,
    SheetSchema,
)

router = Router(tags=["sheets"])


@router.post("/", response=SheetSchema)
def create_sheet(request, payload: SheetIn):
    return Sheet.objects.create(**payload.dict())


@router.get("/", response=List[SheetSchema])
def list_sheets(request):
    return Sheet.objects.all()


@router.get("/{sheet_id}", response=SheetSchema)
def get_music(request, sheet_id: int):
    return get_object_or_404(Sheet, id=sheet_id)


@router.put("/{sheet_id}", response=SheetSchema)
def update_music(request, sheet_id: int, payload: SheetIn):
    sheet = get_object_or_404(Sheet, id=sheet_id)
    for attr, value in payload.dict().items():
        setattr(sheet, attr, value)
    sheet.save()
    return sheet


@router.delete("/{sheet_id}", response={204: None})
def delete_sheet(request, sheet_id: int):
    sheet = get_object_or_404(Sheet, id=sheet_id)
    sheet.delete()
