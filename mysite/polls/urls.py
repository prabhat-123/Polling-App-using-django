from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.home),
    path('<int:question_id>/', views.detail),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    path('<int:question_id>/results/', views.results, name="results"),
]


