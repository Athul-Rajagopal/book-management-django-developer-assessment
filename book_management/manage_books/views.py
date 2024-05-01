from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, ReadingList
from .serializers import BookSerializer, ReadingListSerializer

# Create your views here.

# Fetching list of books and creating new book object 
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    

# Fetching and deleting specific book data
class BookDetail(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Fetching and Creating Reading lists
class ReadingListAPI(generics.ListCreateAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Fetching, arranging and deleting a specific reading list
class ReadingListDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]