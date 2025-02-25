from django.urls import path

from . import views

app_name = "students"
urlpatterns = [
    path("", views.index, name="index"),
    path("students/", views.student_list, name="student_list"),
    path("students/<int:student_id>/", views.student_page, name="student_page"),
    path("groups/", views.group_list, name="group_list"),
    path("groups/<int:group_id>/", views.group_page, name="group_page"),
    path('reg/', views.registration, name='reg')
]