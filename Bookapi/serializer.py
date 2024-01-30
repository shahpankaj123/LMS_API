from rest_framework import serializers
from .models import Book,BookDetails,BorrowedBooks


class AddBookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=13)
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=100)
    number_of_pages = serializers.IntegerField()
    publisher = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=50)    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'  



class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = '__all__'


class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['return_date']


class BorrowedBooksListSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = BorrowedBooks
        fields = '__all__'
