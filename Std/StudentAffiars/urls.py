from django.urls import path
from . import views

urlpatterns = [
    path("", views.newHome, name = "newhome"),
    path("home", views.home, name = "home"),
    path("add" ,views.add ,name = "add"),
    path("view", views.view, name = "view"),
    path("edit/<int:id>", views.edit, name = "edit"),
    path("update/<int:id>", views.update, name = "update"),
    path("assign", views.assign, name = "assign"),
    path("assigndepartment/<int:id>", views.assigndep, name="assigndepartment"),
    path("activeStudents", views.activeStudents, name = "activeStudents"),
   # path("delete", views.delete, name = "delete")
    path("changeActive", views.changeActive, name = "changeActive")
    
]