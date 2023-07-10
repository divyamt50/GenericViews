from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'main_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name = 'main'),
    path('cat/', CatsView.as_view(), name = 'cat_list'),
    path('cat/<int:pk>/', CatDescription.as_view(), name = 'cat_detail'),
]
