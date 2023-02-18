from . import views
from django.urls import path

urlpatterns = [
    path("", views.index.as_view(), name="main_page"),
    path("<int:id>", views.delete_challenge, name="delete_challenge_page")
]
