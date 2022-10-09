from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path('project/<int:id>',views.details,name ="details"),
    path('project/results/<int:id>',views.results,name ="results"),
    path('project/searchresults/<str:keyword>/',views.searchresults,name ="searchresults"),
]
