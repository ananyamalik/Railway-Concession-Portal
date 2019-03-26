from django.urls import path
from .views import (
student_list, student_add, student_profile,first_page,college_login,student_login,student_profile, webcam, railway_login, login)

app_name = 'college'

urlpatterns = [
    path('hp/',first_page,name='page'),
    path('',student_list,name = 'list'),
    path('add/', student_add, name='add'),
    path('profile/<int:id>',student_profile, name='profile'),
    path('hp/collegelogin/',college_login, name='collegelogin'),
    path('studentlogin/',student_login, name='studentlogin'),
    path('railwaylogin',railway_login, name='railwaylogin'),
    path('hp/login',login, name='profile'),
    path('webimg/',webcam, name='profile'),

]
