from typing import List

from ninja import Query, Router
from ninja.pagination import PageNumberPagination, paginate

from musics.models import Music

from .schemas import (
    MultiMusicFilters,
    MusicCustomExpressionFilterSchema,
    MusicCustomExpressionRefactorFilterSchema,
    MusicFilter_Gt_10_Schema,
    MusicFilterContainsIgnoreCaseSchema,
    MusicFilterSchema,
    MusicOut,
    MusicSchema,
)

router = Router(tags=["musics_other"])


@router.get("/get_multi_musics", response=List[MusicSchema])
def get_multi_musics(request, filters: Query[MultiMusicFilters]):
    music_ids = filters.dict().get("music_ids")
    music = Music.objects.filter(id__in=music_ids)
    return music


@router.get("/paginate_list", response=List[MusicOut])
@paginate
def list_paginate(request):
    return Music.objects.all()


@router.get("/paginate_page", response=List[MusicOut])
@paginate(PageNumberPagination, page_size=2)
def page_paginate(request):
    return Music.objects.all()


@router.get("/list_music_filter", response=List[MusicOut])
def list_music_filter(request, filters: MusicFilterSchema = Query(...)):
    musics = Music.objects.all()
    musics = filters.filter(musics)

    # look raw sql
    # print(musics.query)

    return musics


@router.get("/list_music_custom_expression_filter", response=List[MusicOut])
def list_music_custom_expression_filter(
    request,
    filters: MusicCustomExpressionFilterSchema = Query(...),
):
    musics = Music.objects.all()
    musics = filters.filter(musics)

    # look raw sql
    print(musics.query)

    return musics


@router.get("/list_music_custom_expression_refactor_filter", response=List[MusicOut])
def list_music_custom_expression_refactor_filter(
    request,
    filters: MusicCustomExpressionRefactorFilterSchema = Query(...),
):
    musics = Music.objects.all()
    musics = filters.filter(musics)

    # look raw sql
    print(musics.query)

    return musics


@router.get("/list_music_contains_ignore_case_filter", response=List[MusicOut])
def list_music_contains_ignore_case_filter(
    request, filters: MusicFilterContainsIgnoreCaseSchema = Query(...)
):
    musics = Music.objects.all()
    musics = filters.filter(musics)

    # look raw sql
    # print(musics.query)

    return musics


@router.get("/list_music_gt_10_filter", response=List[MusicOut])
def list_music_gt_10_filter(request, filters: MusicFilter_Gt_10_Schema = Query(...)):
    musics = Music.objects.all()
    musics = filters.filter(musics)

    # look raw sql
    # print(musics.query)

    return musics
