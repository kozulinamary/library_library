from django.urls import path
from .endpoints import AuthorListAPIView,\
    AuthorListCreateAPIView, AuthorDetailAPIView,\
    AuthorUpdateAPIView, AuthorDestroyAPIView, AuthorRUDAPIView, BookListAPIView,\
    BookListCreateAPIView, BookDetailAPIView, BookUpdateAPIView, BookDestroyAPIView, BookRUDAPIView


urlpatterns = [
    path('author_list/', AuthorListAPIView.as_view(), name='author_list'),
    path("books_list/", BookListAPIView.as_view(), name="book_list"),
    path('author_create/', AuthorListCreateAPIView.as_view(), name='author_create'),
    path("book_create/", BookListCreateAPIView.as_view(), name="book_create"),
    path("author_detail/<int:pk>", AuthorDetailAPIView.as_view(), name="author_detail"),
    path("book_detail/<int:pk>", BookDetailAPIView.as_view(), name="book_detail"),
    path("author_update/<int:pk>", AuthorUpdateAPIView.as_view(), name="author_update"),
    path("book_update/<int:pk>", BookUpdateAPIView.as_view(), name="book_update"),
    path("author_destroy/<int:pk>", AuthorDestroyAPIView.as_view(), name="author_destroy"),
    path("book_destroy/<int:pk>", BookDestroyAPIView.as_view(), name="book_destroy"),
    path("author_rud/<int:pk>", AuthorRUDAPIView.as_view(), name="author_rud"),
    path("book_rud/<int:pk>", BookRUDAPIView.as_view(), name="book_rud"),
]
