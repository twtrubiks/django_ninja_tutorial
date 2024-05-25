# django ninja 教學

官網介紹 [Django Ninja - Fast Django REST Framework](https://django-ninja.dev/)

基本上, Django Ninja 就是在 django 上多加東西而已, 有超強的 pydantic, 也可以自動產生文件,

更支援 django 原生的 ORM, 非常建議大家玩玩看.

這邊寫了一些範例, 建議大家直接進去 docs 裡面看.

## 使用方法

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

## 其他

- [Async support](https://django-ninja.dev/guides/async-support/)

## 執行環境

- Python 3.12

- VSCode

## Reference

- [Django Ninja - Fast Django REST Framework](https://django-ninja.dev/)

- [Django Ninja Extra](https://eadwincode.github.io/django-ninja-extra/)

- [Ninja JWT](https://eadwincode.github.io/django-ninja-jwt/)