from django.urls import path, include
from . import views

urlpatterns = [
    path('question', views.Question_list),
    path(r'question/<int:id>', views.Question_lookup),
]
