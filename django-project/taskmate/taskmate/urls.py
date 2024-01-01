from django.contrib import admin
from django.urls import include, path
from todo_app import views as todo_views
from users_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todo_views.index, name="index"),
    path("todolist/", include("todo_app.urls")),
    path("account/", include("users_app.urls")),
    path("contact/", todo_views.contact, name="contact"),
    path("about/", todo_views.about, name="about"),
]
