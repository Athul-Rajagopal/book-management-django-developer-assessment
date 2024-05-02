from rest_framework import serializers
from .models import Book, ReadingList, ReadingListItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'description']
        
        
        



      

class ReadingListSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = ReadingList
        fields = ['id', 'name', 'books']

    def get_books(self, obj):
        # Retrieve the books and their orders for the current reading list
        reading_list_items = ReadingListItem.objects.filter(reading_list=obj)
        # Serialize each book along with its order
        return [{'id': item.book.id,
                 'title': item.book.title,
                 'authors': item.book.authors,
                 'genre': item.book.genre,
                 'publication_date': item.book.publication_date,
                 'description': item.book.description,
                 'order': item.order} for item in reading_list_items]
