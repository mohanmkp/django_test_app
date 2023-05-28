from .import views
from django.urls import path

urlpatterns = [
    path("", views.UserAction.as_view()),
    path("signin/", views.SingIn.as_view()),


]

