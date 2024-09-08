from .models import Author, Book
from rest_framework import serializers

# BookSerializer makes sure that the book has its publicatin year in a meaningful year so it is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['publication_year'] > 2024:
            raise serializers.ValidationError("publication year cannot be in the future")
        return data



class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many =True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']