from django.shortcuts import render
from account.models import User
from django.shortcuts import get_object_or_404
from .models import Book,BookDetails,BorrowedBooks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AddBookSerializer,BookSerializer,BookDetailsSerializer,BorrowedBooksSerializer,ReturnBookSerializer,BorrowedBooksListSerializer

class AddBookView(APIView):
    def post(self, request, format=None):
        serializer = AddBookSerializer(data=request.data)
        if serializer.is_valid():
            book_data = serializer.validated_data
            new_book = Book.objects.create(
                title=book_data['title'],
                isbn=book_data['isbn'],
                published_date=book_data['published_date'],
                genre=book_data['genre']
            )
            BookDetails.objects.create(
                book=new_book,
                number_of_pages=book_data['number_of_pages'],
                publisher=book_data['publisher'],
                language=book_data['language']
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListAllBooksView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetBookByIDView(APIView):
    def get(self, request, book_id, format=None):
        book = get_object_or_404(Book, book_id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
class AssignUpdateBookDetailsView(APIView):
    def post(self, request, book_id, format=None):
        book = get_object_or_404(Book, book_id=book_id)
        book_details_data = request.data.get('book_details', {})
        serializer = BookDetailsSerializer(data=book_details_data)

        if serializer.is_valid():
            book_details, created = BookDetails.objects.get_or_create(book=book)
            
            book_details.number_of_pages = serializer.validated_data.get('number_of_pages', book_details.number_of_pages)
            book_details.publisher = serializer.validated_data.get('publisher', book_details.publisher)
            book_details.language = serializer.validated_data.get('language', book_details.language)
            book_details.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class BorrowBookView(APIView):
    def post(self, request, book_id, user_id, format=None):
        book = get_object_or_404(Book, book_id=book_id)
        user = get_object_or_404(User, id=user_id)

        borrow_data = {
            'user': user.id,
            'book': book.id,
            'borrow_date': request.data.get('borrow_date'),
            'return_date': request.data.get('return_date'),
        }

        serializer = BorrowedBooksSerializer(data=borrow_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class ReturnBookView(APIView):
    def put(self, request, borrowed_books_id, format=None):
        borrowed_book = get_object_or_404(BorrowedBooks, id=borrowed_books_id)
        serializer = ReturnBookSerializer(borrowed_book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAllBorrowedBooksView(APIView):
    def get(self, request, format=None):
        borrowed_books = BorrowedBooks.objects.all()
        serializer = BorrowedBooksListSerializer(borrowed_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)        