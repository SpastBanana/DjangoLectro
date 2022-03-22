from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('home', views.homeView, name="home"),
    path('portfolio', views.portfolioView, name="portfolio"),
    path('over-DataLectro', views.portfolioView, name="over-DataLectro"),
    path('contact', views.contactView, name="contact"),
    path('elektra', views.portfolioView, name="elektra"),
    path('engineering', views.portfolioView, name="engineering"),
    path('ICT-IOT', views.portfolioView, name="ict"),
    path('solar', views.portfolioView, name="solar"),
]
