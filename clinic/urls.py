from django.urls import path , include
from . import views
app_name='clinic'

urlpatterns = [
    path('',views.service_list),
    path('make_order',views.make_order,name='make_order'),
    path('team',views.team,name='team'),
    path('price',views.price,name='prices'),
    path('make_time',views.appointment,name='time'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('about',views.about_us,name='about'),



]
