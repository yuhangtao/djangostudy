from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns=[
    path('',views.index),
    path('grades/',views.grades),
    path('students',views.student),
    url(r'grades/(\d+)',views.gradestudent),
    url(r'^get1',views.get1),
    url(r'^showregister/register/$',views.register),
    url(r'^showregister/$',views.showregister),
    url(r'^testcookie/$',views.testcookie),
    url(r'^redirect1/$',views.redirect1),
    url(r'^showmain/$', views.showmain),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^quit/$',views.quit),
    url(r'^upfile/$',views.upfile),
    url(r'^savefile/$',views.savefile),
    url(r'^edit/$',views.edit)


]