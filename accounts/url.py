# import
from django.urls import path
from . import views

# create accounts/parts url

urlpatterns = [
    path('parts-search/', views.parts_search_page),
    path("api/parts/", views.search_parts),
]
