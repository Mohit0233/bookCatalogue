from django.urls import path
from authors import views


urlpatterns = [
    path('addAnAuthor', views.AddAnAuthor.as_view()),
    path('getAllAuthorName', views.GetAllAuthorName.as_view())
]