# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice route creation, request handling, and in-memory data management.

## 📝 Tasks

### 🛠️ [Create the FastAPI App and Core Endpoints]

#### Description
Set up a FastAPI application for a small book catalog. Implement endpoints to list all books and retrieve a single book by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Define an in-memory list of books with at least 3 sample items.
- Implement `GET /books` to return the full list of books.
- Implement `GET /books/{book_id}` to return one book by ID.
- Return a clear error response when a book ID does not exist.


### 🛠️ [Add Create and Delete Operations]

#### Description
Extend the API to support creating and deleting books. Validate incoming data and return appropriate status codes.

#### Requirements
Completed program should:

- Implement `POST /books` to add a new book.
- Use a Pydantic model to validate input fields.
- Automatically assign a new unique ID for each created book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return meaningful success and error messages with suitable HTTP status codes.
