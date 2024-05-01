from rest_framework import serializers
from .models import Book, ReadingList, ReadingListItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'description']
        

class ReadingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListItem
        fields = ['book', 'order']

class ReadingListSerializer(serializers.ModelSerializer):
    books = ReadingListItemSerializer(many=True)

    class Meta:
        model = ReadingList
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books')
        reading_list = ReadingList.objects.create(**validated_data)
        for book_data in books_data:
            ReadingListItem.objects.create(reading_list=reading_list, **book_data)
        return reading_list