from django.db import models


class Sheet(models.Model):
    name = models.CharField(default="sheet name")

    class Meta:
        db_table = "sheet"


class Music(models.Model):
    song = models.CharField(default="my song")
    singer = models.CharField(default="my singer")
    count = models.IntegerField(default=0)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, null=True, blank=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"
