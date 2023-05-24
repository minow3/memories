from django.urls import path
from . import views

app_name = 'share'


urlpatterns = [
    path('', views.ListImageView.as_view(), name='list'),
    path('upload/', views.UploadImageView.as_view(), name='upload')
]