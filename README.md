
## Library Management System

This project is a Library Management System developed using Django, showcasing models with 1-1, 1-M, and M-M relationships. It includes APIs to interact with these models.

## Project Overview

The project is built using Django, a high-level Python web framework. It implements a Library Management System with the following features:
- User model with a 1-M relationship with BorrowedBooks.
- Book model with a 1-1 relationship with BookDetails and a 1-M relationship with BorrowedBooks.
- BookDetails model for 1-1 relationship with Book.
- BorrowedBooks model to demonstrate a 1-N relationship with User and Book.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone git@github.com:shahpankaj123/LMS_API.git
   cd LMS_API
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate.bat if using cmd else .ps1`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```
   
## JWT Authentication
   JWT (JSON Web Token) authentication is used to secure API endpoints. 
   
## Database Schema Design

The database schema includes the following models:

1. **User Model:**
   - Attributes: UserID, Name, Email, MembershipDate
   - Relationships: 1-M with BorrowedBooks
   - Used Jwt Authentication

2. **Book Model:**
   - Attributes: BookID, Title, ISBN, PublishedDate, Genre
   - Relationships: 1-1 with BookDetails, 1-M with BorrowedBooks

3. **BookDetails Model:**
   - Attributes: DetailsID, BookID (FK), NumberOfPages, Publisher, Language
   - Relationships: 1-1 with Book

4. **BorrowedBooks Model:**
   - Attributes: UserID (FK), BookID (FK), BorrowDate, ReturnDate
   - Relationships: 1-M with User

## API Development

The APIs are implemented using Django REST framework. Here are the endpoints:

 1. **User Registration:**
   - Endpoint: `http://127.0.0.1:8000/api/user/register/`
   - View: `UserRegisterView`
   - Description: Allows users to register with the system.

2. **User Login:**
   - Endpoint: `http://127.0.0.1:8000/api/user/login/`
   - View: `UserLoginView`
   - Description: Provides a login interface for users.

3. **User Profile Detail:**
   - Endpoint: `http://127.0.0.1:8000/api/user/Userdetail/`
   - View: `Profileview`
   - Description: Displays the user's profile details.

4. **Change Password:**
   - Endpoint: `http://127.0.0.1:8000/api/user/changepassword/`
   - View: `UserchangepasswordView`
   - Description: Allows users to change their password.

5. **Send Mail:**
   - Endpoint: `http://127.0.0.1:8000/api/user/sendmail/`
   - View: `UserSendMailView`
   - Description: Sends an email to the user.

6. **Password Reset:**
   - Endpoint: `http://127.0.0.1:8000/api/user/reset/<uid>/<token>`
   - View: `UserPasswordResetView`
   - Description: Resets the user's password using a unique token.

7. **All User Profiles:**
   - Endpoint: `http://127.0.0.1:8000/api/user/allUserdetail/`
   - View: `All_UserProfileView`
   - Description: Lists all user profiles.

8. **User Profile by ID:**
   - Endpoint: `http://127.0.0.1:8000/api/user/Userdetail/<id>/`
   - View: `UserProfile_ByIDView`
   - Description: Displays the profile of a specific user identified by ID.
   - Attributes: UserID, Name, Email, MembershipDate
   - Relationships: 1-M with BorrowedBooks
     
9. **Add Book:**
   - Endpoint: `http://127.0.0.1:8000/book/add_book/`
   - View: `AddBookView`
   - Description: Allows users to add a new book to the library.

10. **List All Books:**
   - Endpoint: `http://127.0.0.1:8000/book/list_all_books/`
   - View: `ListAllBooksView`
   - Description: Lists all books currently available in the library.

11. **Get Book by ID:**
   - Endpoint: `http://127.0.0.1:8000/book/get_book/<int:book_id>/`
   - View: `GetBookByIDView`
   - Description: Retrieves details of a specific book using its ID.

12. **Assign/Update Book Details:**
   - Endpoint: `http://127.0.0.1:8000/book/assign_update_book_details/<int:book_id>/`
   - View: `AssignUpdateBookDetailsView`
   - Description: Allows assigning or updating details of a specific book, like the number of pages, publisher, and language.

13. **Borrow a Book:**
   - Endpoint: `http://127.0.0.1:8000/book/borrow_book/<int:book_id>/<int:user_id>/`
   - View: `BorrowBookView`
   - Description: Records the borrowing of a book by linking a user with a book.

14. **Return a Book:**
   - Endpoint: `http://127.0.0.1:8000/book/return_book/<int:borrowed_books_id>/`
   - View: `ReturnBookView`
   - Description: Updates the system when a book is returned.

15. **List All Borrowed Books:**
   - Endpoint: `http://127.0.0.1:8000/book/list_all_borrowed_books/`
   - View: `ListAllBorrowedBooksView`
   - Description: Lists all books currently borrowed from the library.


## Testing and Validation

Test each API endpoint using tools like Postman or `curl`. Ensure that CRUD operations work as intended.

## Code Quality and Error Handling

The code is organized, readable, and well-documented. Robust error handling is implemented to cover edge cases and potential errors.

Feel free to customize the project according to your requirements and add additional features as needed.
```

This version focuses solely on the project details and setup instructions, excluding the submission instructions and bonus section.

