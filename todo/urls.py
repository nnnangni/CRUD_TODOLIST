from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # create
    path("new/", views.new),
    path("create/", views.create),
    # read
    path("<int:id>/", views.read),
    # update
    path("<int:id>/edit/", views.edit),
    path("<int:id>/update/", views.update),
    # delete
    path("<int:id>/delete/", views.delete),
    
]