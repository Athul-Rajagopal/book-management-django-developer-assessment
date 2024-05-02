from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, ReadingList, ReadingListItem
from .serializers import BookSerializer, ReadingListSerializer
from django.shortcuts import get_object_or_404


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
    
    
    
# Fetching reading lists
class ReadingListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all reading lists
        reading_lists = ReadingList.objects.all()
        # Serialize the reading lists
        serializer = ReadingListSerializer(reading_lists, many=True)
        return Response(serializer.data)


# Creating Reading lists
class ReadingListCreate(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        books_data = data.get('books', [])
        # Get the current authenticated user
        user = request.user

        # Create ReadingList associated with the current user
        reading_list = ReadingList.objects.create(name=name, user=user)

        # Fetch existing Book instances and add them to the reading list
        for book_data in books_data:
            book_title = book_data.get('title')
            book_instance = get_object_or_404(Book, title=book_title)
            ReadingListItem.objects.create(reading_list=reading_list, book=book_instance, order=book_data['order'])

        
        return Response({'message':'Reading list created successfully'}, status=status.HTTP_201_CREATED)



# Fetching, arranging and deleting a specific reading list
class ReadingListDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]