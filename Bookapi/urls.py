from django.urls import path
from .views import AddBookView, ListAllBooksView, GetBookByIDView, AssignUpdateBookDetailsView,BorrowBookView,ReturnBookView,ListAllBorrowedBooksView

urlpatterns = [
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('list_all_books/', ListAllBooksView.as_view(), name='list_all_books'),
    path('get_book/<int:book_id>/', GetBookByIDView.as_view(), name='get_book_by_id'),
    path('assign_update_book_details/<int:book_id>/', AssignUpdateBookDetailsView.as_view(), name='assign_update_book_details'),
    path('borrow_book/<int:book_id>/<int:user_id>/', BorrowBookView.as_view(), name='borrow_book'),
    path('return_book/<int:borrowed_books_id>/', ReturnBookView.as_view(), name='return_book'),
    path('list_all_borrowed_books/', ListAllBorrowedBooksView.as_view(), name='list_all_borrowed_books'),
]
