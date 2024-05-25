from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from musics.models import Music, Sheet

from .schemas import CreateMusicSchema, MusicIn, MusicOut, MusicSchema

router = Router(tags=["musics"])


@router.post("/", response=MusicOut)
def create_music(request, payload: CreateMusicSchema):
    music = Music.objects.create(**payload.dict())
    return music


@router.get("/", response=List[MusicOut])
def list_musics(request):
    return Music.objects.all()


@router.get("/{music_id}", response=MusicSchema)
def get_music(request, music_id: int):
    music = get_object_or_404(Music, id=music_id)
    return music


@router.put("/{music_id}", response=MusicSchema)
def update_music(request, music_id: int, payload: MusicIn):
    music = get_object_or_404(Music, id=music_id)
    if sheet_id := payload.sheet:
        sheet = get_object_or_404(Sheet, id=sheet_id)
        music.sheet = sheet

    music.song = payload.song
    music.singer = payload.singer
    music.count = payload.count
    music.save()
    return music


@router.delete("/{music_id}", response={204: None})
def delete_music(request, music_id: int):
    music = get_object_or_404(Music, id=music_id)
    music.delete()
