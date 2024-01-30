from django.db import models
from account.models import User

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class BookDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='details')
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.book.title} - Details"


class BorrowedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} - {self.book.title}"


