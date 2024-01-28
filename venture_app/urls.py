from django.urls import path
from venture_app import views

app_name = "venture_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_info/', views.contact_info, name='contact_info'),
    path('people/', views.people, name='people'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('news/', views.news, name='news'),
    path('investment-process/', views.investment_process, name='investment_process'),

]