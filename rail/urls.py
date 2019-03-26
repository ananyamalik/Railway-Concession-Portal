from django.urls import path
from .views import ( student_list, student_add, student_profile,student_delete )

app_name = 'college'

urlpatterns = [
    path('list/',student_list,name = 'list'),
    path('list/add/', student_add, name='add'),
    path('list/profile/<int:id>',student_profile, name='profile'),
    path('list/profile/delete/<int:id>',student_delete, name='delete'),
]
