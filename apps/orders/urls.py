from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.OrderProduct.as_view()),


]

