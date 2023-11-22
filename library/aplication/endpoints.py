from rest_framework.generics import ListAPIView,\
    ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView,\
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorListCreateAPIView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorDetailAPIView(RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()






class AuthorDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
class AuthorRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()