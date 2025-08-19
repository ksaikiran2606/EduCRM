# student/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.student_panel, name='student_panel'),
    path('panel/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('panel/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('list/', views.student_panel, name='student_list'),
]