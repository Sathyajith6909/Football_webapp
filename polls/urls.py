from django.urls import path
from . import views


urlpatterns = [
    path('welcome', views.Front_page, name='hellos'),
    path('log', views.login_1, name='login_1'),
    path('logout', views.logout_view, name='logout_view'),
    path('teamrg', views.insert_Team, name='insert_Team'),
    path('smaker', views.Schedule_maker, name='Schedule_maker'),
    path('squader', views.squad, name='squad'),
    path('schedule_list', views.schedulelist, name='schedulelist'),
    path('schedule_listad', views.schedulelistadmin, name='schedulelistadmin'),
    path('update_u/<int:requested_blog_id>', views.update_u, name='update_u'),
    

]
