from django.contrib import admin
from django.urls import path, include


# jadi disini terdapat perbedaan yang dimaan terdapat url ke admin dan juga terdapat url untuk mengakses aplikasi 'app' yang telah dibuat sebelumnya.
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('app.urls')),  # Include app URLs
]
