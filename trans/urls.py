from django.urls import path
from . import views

app_name = 'trans'
urlpatterns = [
    # ex: /trans/
    path('', views.index, name='index'),
    path('ans/', views.ans, name='ans')
]
