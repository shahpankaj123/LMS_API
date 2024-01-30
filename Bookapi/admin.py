from django.contrib import admin
from .models import Book,BookDetails,BorrowedBooks

# Register your models here.
admin.site.register(Book)
admin.site.register(BookDetails)
admin.site.register(BorrowedBooks)

