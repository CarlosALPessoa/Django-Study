from django.contrib import admin # type: ignore
from django.urls import path, include #type: ignore

urlpatterns = [
    path('', include("home.urls")),
    path('blog/', include("blog.urls")),
    path("admin/", admin.site.urls)
]
