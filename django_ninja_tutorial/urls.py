"""
URL configuration for django_ninja_tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

# from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from example.api import router as example_router
from musics.api_music import router as musics_router
from musics.api_other import router as others_router
from musics.api_sheet import router as sheets_router
from ninja_extra_api_tutorial.api import JWTController, MyAPIController
from utils.exception import ServiceUnavailableError

# api = NinjaAPI()

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController, JWTController)

api.add_router("/examples/", example_router)
api.add_router("/sheets/", sheets_router)
api.add_router("/musics/", musics_router)
api.add_router("/others/", others_router)

# NinjaExtraAPI
api.register_controllers(MyAPIController)


@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": "Please retry later"},
        status=503,
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
