from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('blog.urls')),
    path('evaluacion2/', views.evaluacion2, name='evaluacion2'),
]
