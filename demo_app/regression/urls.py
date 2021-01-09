from django.urls import path
from . import views

app_name = "regression"
urlpatterns = [
    path("", views.index, name="index"),
    path("upload_file", views.upload_file, name="uploadcsv"),
    path("datatable", views.datatable, name="datatable"),
    path("eda", views.eda, name="eda")
]