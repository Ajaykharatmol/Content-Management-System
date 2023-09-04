from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path("", views.index, name="index"),
    path('CreateUserRegister', views.CreateUserRegister.as_view()),
    path('LoginUser', views.AppToken.as_view()),
    path('Author', views. AuthorList.as_view()),
    path('Author/<int:pk>', views. AuthorDetail.as_view()),
    path('search', views.SearchView.as_view(), name="search_view"),

]

urlpatterns = format_suffix_patterns(urlpatterns)