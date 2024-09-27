# django ninja 教學

官網介紹 [Django Ninja - Fast Django REST Framework](https://django-ninja.dev/)

基本上, Django Ninja 就是在 django 上多加東西而已,

有超強的 [pydantic 教學](https://github.com/twtrubiks/python-notes/tree/master/pydantic_tutorial), 也可以自動產生文件,

更支援 django 原生的 ORM, 非常建議大家玩玩看 😄

這邊寫了一些範例, 建議大家直接進去 docs 裡面看.

目錄

- [Ninja 使用方法](#Ninja-使用方法)

- [Django Ninja Extra](#django-ninja-extra)

- [Ninja JWT](#ninja-jwt)

- [Sending email 搭配 Mailpit](#sending-email-搭配-mailpit---email-testing-for-developers)

- [Django admin example](#django-admin-example)

## Ninja 使用方法

安裝 dev-containers, `>Dev Containers: Rebuild and Reopen in Container`

如果不熟悉請參考 [Vscode Dev Containers 教學](https://github.com/twtrubiks/vscode_python_note?tab=readme-ov-file#vscode-dev-containers-%E6%95%99%E5%AD%B8)

先 migrate

```cmd
python3 manage.py migrate
```

執行 django ninja

```cmd
./manage.py runserver
```

接著進入 doc [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)

如果你想玩玩, 直接在這個頁面上操作即可.

example 基本上就是一些範例, 沒有和 db 互動.

sheets, musics 有和 db 互動, 並且有 ORM 的操作.

musics_other 有和 db 互動, 並且有比較複雜的 ORM 操作, 以及 django ninja [Filtering](https://django-ninja.dev/guides/input/filtering/) 的用法.

![alt tag](https://i.imgur.com/Ga0Hohi.png)

## Django Ninja Extra

[Django Ninja Extra](https://eadwincode.github.io/django-ninja-extra/)

更方便定義 api, 範例如下

[ninja_extra_api_tutorial](ninja_extra_api_tutorial)

THROTTLE

![alt tag](https://i.imgur.com/EWr2DQ5.png)

## Ninja JWT

[Ninja JWT](https://eadwincode.github.io/django-ninja-jwt/)

定義 JWT, 範例如下

![alt tag](https://i.imgur.com/6u97gtR.png)

![alt tag](https://i.imgur.com/xnWfQjW.png)

如果你想要設定黑名單, 可以使用 [Blacklist App](https://eadwincode.github.io/django-ninja-jwt/blacklist_app/),

使用 django admin 模擬將 refresh token 加進去黑名單, 這樣就可以強制 user 重新取 refresh token 了.

或是使用 `token.blacklist()` 加入黑名單,

可參考範例 `/api/auth/blacklist` 這個 api.

db 中 `token_blacklist_outstandingtoken` 紀錄 refresh token.

db 中 `token_blacklist_blacklistedtoken` 紀錄 blacklisted token.

## Sending email 搭配 Mailpit - email testing for developers

這部份就和 Ninja 沒關係了, 單純就是 Django 而已,

一般 django 開發要寄信, 需要設定 [settings.py](https://github.com/twtrubiks/django_ninja_tutorial/blob/main/django_ninja_tutorial/settings.py)

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

然後去 call api `post` `/api/examples/send_email` (簡單的範例)

接著看你的 console log

![alt tag](https://i.imgur.com/VpsyJ3l.png)

那這時候, 有沒有比較好的方式可以看這些信 ❓

有的 😀

就是我們要介紹的 [Mailpit - email testing for developers](https://github.com/axllent/mailpit) (UI 也不錯看 😁),

[docker-compose.yml](docker-compose.yml) 這部份加上

```yml
......
  mailpit:
    image: axllent/mailpit
    restart: unless-stopped
    ports:
       - "8025:8025"
       - "1025:1025"
......
```

Django 需要修改設定 [settings.py](https://github.com/twtrubiks/django_ninja_tutorial/blob/main/django_ninja_tutorial/settings.py)

```python
# use mailpit
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailpit" # 對應 docker容器的 service
EMAIL_PORT = 1025 # 定義為 1025
```

然後再去 call api `post` `/api/examples/send_email`

然後 console log 就不會再像之前一樣顯示了, 現在會顯示在 [http://127.0.0.1:8025/](http://127.0.0.1:8025/)

![alt tag](https://i.imgur.com/iZpfI3B.png)

點進去也會有更詳細的資訊

![alt tag](https://i.imgur.com/cug1aBW.png)

## Django admin example

一般的 Django 操作完全可以正常使用, 像是這邊我們來撰寫 Django [admin.py](https://github.com/twtrubiks/django_ninja_tutorial/blob/main/musics/admin.py),

使用 [formfield_overrides](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.formfield_overrides)

```python
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {
            "widget": forms.TextInput(attrs={"style": "width: 500px; height: 50px;"})
        },
    }
```

成功覆寫了 style ( 把它拉長拉寬了 )

![alt tag](https://i.imgur.com/EWuHkp5.png)

## 其他

- [Async support](https://django-ninja.dev/guides/async-support/)

## 執行環境

- Python 3.12

- VSCode

## Reference

- [Django Ninja - Fast Django REST Framework](https://django-ninja.dev/)

- [Django Ninja Extra](https://eadwincode.github.io/django-ninja-extra/)

- [Ninja JWT](https://eadwincode.github.io/django-ninja-jwt/)