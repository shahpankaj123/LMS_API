Certainly! Here's an updated README.md without the submission instructions and bonus section:

```markdown
# Library Management System

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
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
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

## Database Schema Design

The database schema includes the following models:

1. **User Model:**
   - Attributes: UserID, Name, Email, MembershipDate
   - Relationships: 1-M with BorrowedBooks

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

1. **User APIs:**
   - `POST /api/users/`: Create a new user.
   - `GET /api/users/`: List all users.
   - `GET /api/users/<user_id>/`: Get user details by ID.

2. **Book APIs:**
   - `POST /api/books/`: Add a new book.
   - `GET /api/books/`: List all books.
   - `GET /api/books/<book_id>/`: Get book details by ID.
   - `PUT /api/books/<book_id>/details/`: Assign/update book details.

3. **BorrowedBooks APIs:**
   - `POST /api/borrow/`: Borrow a book.
   - `PUT /api/return/<borrowed_id>/`: Return a book.
   - `GET /api/borrowed-books/`: List all borrowed books.

## Testing and Validation

Test each API endpoint using tools like Postman or `curl`. Ensure that CRUD operations work as intended.

## Code Quality and Error Handling

The code is organized, readable, and well-documented. Robust error handling is implemented to cover edge cases and potential errors.

Feel free to customize the project according to your requirements and add additional features as needed.
```

This version focuses solely on the project details and setup instructions, excluding the submission instructions and bonus section.

