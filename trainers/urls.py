from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainerList, name="alltrainers"),
    path('addtrainer/', views.addTrainers, name="addtrainer"),
    path('update_trainer/<str:id>', views.update_trainer, name="update"),
    path("delete/<str:id>", views.delete_trainer, name='delete'),
]
