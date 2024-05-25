from ninja_extra import api_controller, http_get, http_post, throttle
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import RefreshToken

from ninja_extra_api_tutorial.schemas import DivideItem


# class based definition
@api_controller("/extra", tags=["extra"], permissions=[])
class MyAPIController:
    @http_get("/subtract")
    def subtract(self, a: int, b: int):
        """Subtracts a from b"""
        return {"result": a - b}

    @http_post("/divide")
    def divide(self, data: DivideItem):
        return f"hello {data.name}"

    @http_get("/hello")
    @throttle
    def hello(self):
        return "hello"


@api_controller("/auth", tags=["jwt"], permissions=[], auth=JWTAuth())
class JWTController:
    @http_get("/hello")
    def hello(self):
        return "hello"

    @http_post("/blacklist")
    def blacklist(self, request):
        for obj in request.user.outstandingtoken_set.all():
            try:
                refresh_token = RefreshToken(obj.token)
                refresh_token.blacklist()
            except Exception:
                pass

        return f"blacklist {request.user} All RefreshToken"
