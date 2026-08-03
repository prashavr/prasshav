from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app1.urls")),

]

#browser url call -->  proejct.urls file ma check if the route exists or not
#broser/ user --> url --> view --> functions