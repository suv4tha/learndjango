
# testing

from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage),
    path('sign/',views.signIn),
]
