from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


urlpatterns = [
    path("", include("articles.urls")),
    path("", lambda req: redirect("/articles/")),
    path("admin/", admin.site.urls),
]
