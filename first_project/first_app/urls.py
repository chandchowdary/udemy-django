from django.conf.urls import url
from django.contrib import admin
from first_app import views

urlpatterns = [
    url(r'^$',views.first_view, name="first_view"),
    url(r'^users/',views.users, name="users"),
    url(r'^form_page/',views.formclass_view, name = 'formclass_view'),
]
