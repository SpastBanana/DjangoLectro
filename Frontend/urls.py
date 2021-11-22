from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('home/', views.homeView, name="home"),
    path('over-datalectro/', views.overView, name="over-datalectro"),
    path('portfolio/', views.portfolioView, name="portfolio"),
    path('blog/', views.blogView, name="blog"),
    path('het-team/', views.teamView, name="het-team"),
    path('contact/', views.contactView, name="contact"),
    path('elektra/', views.contactView, name="elektra"),
    path('engineering/', views.contactView, name="engineering"),
    path('ict-en-iot/', views.contactView, name="ict"),
    path('solar/', views.solarView, name="solar"),
]
