from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path('devin', views.devin, name="devin"),
    path('isabel', views.isabel, name="isabel"),
    path('<str:name>', views.greet, name="greet")
]