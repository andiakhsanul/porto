from django.urls import path
from app.views import home

# nah disini nantinya link url nya adalah /users/new dikarenakan kita telah menambahkan prefix 'users/' pada urls.py yang ada di folder webporto
urlpatterns = [
    path("", home)
]
