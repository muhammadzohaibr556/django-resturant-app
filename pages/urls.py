from django.urls import path
from .views import *
urlpatterns=[
    path('',homeView,name='home'),
    path('about/',aboutView,name='about'),
    #path('about/',aboutDetailView.as_view(),name='about'),
    path('services/',servicesView,name='services'),
    #path('services/',servicesTemplateView.as_view(),name='services'),
    path('thank/<int:pk>/<str:status>/',thankView,name='thank'),
    path('detail/<int:pk>/',aboutDetailView,name='detail'),
    path('add_home/<int:id>/', cart_add_home, name='cart_add_home'),
    path('remove_home/<int:id>/',cart_remove_home, name = 'cart_remove_home'),
    path('select/<int:id>/',select, name = 'select'),
    path('reserve/',reserve, name = 'reserve'),
    path('hall_charges/<int:id>/',hall_charges, name = 'hall_charges'),
    path('check/',check, name = 'check'),
]