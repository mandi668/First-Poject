from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('category/<id>', views.category, name='category'),
    path('detail/<id>', views.detailItem, name='detail'),
    path("reserve/", views.reserve, name='reserve'),
]
