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
    path('get-investment/', views.get_investment, name='get_investment'),
    path('invest-now/', views.invest_now, name='invest_now'),
    path('our-purpose/', views.our_purpose, name='our_purpose'),
    path('our-business/', views.our_business, name='our_business'),

]