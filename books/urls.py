from django.urls import path
from books import views

urlpatterns = [
    path('addBookToCatalog', views.AddBookToCatalog.as_view()),
    path('addCategory', views.AddCategory.as_view()),
    path('getListOfCategories', views.GetListOfCategories.as_view()),
    path('getMostBooksSoldByAuthor', views.GetMostBooksSoldByAuthor.as_view()),
    path('getMostBooksSoldByCategory', views.GetMostBooksSoldByCategory.as_view()),
    path('searchBook', views.SearchBook.as_view()),
    path('getBooksByAuthor', views.GetBooksByAuthor.as_view()),
]
