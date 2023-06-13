from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('singup/', view=Singup.as_view(), name='singup'),
    path('login/', view=Login.as_view(), name='login'),
    path('logout/', view=Logout.as_view(), name='logout'),
    path('dashborad/', view=Dashborad.as_view(), name='dashborad'),
    path('dashborad/<int:pk>', view=DashboradR.as_view(), name='dashboradR'),
    path('delete_dashboradR/<int:pk>', view=DeleteDashboradR.as_view(), name='delete_dashboradR'),
    path('add_dashboradR/', view=AddDashboradR.as_view(), name='add_dashboradR'),
    path('update_dashboradR/<int:pk>', view=Update_dashboradR.as_view(), name='update_dashboradR'),

]
