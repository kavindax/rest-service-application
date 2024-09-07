# rest-service-application

REST Service application

## Create a book

curl -X POST "http://localhost:8000/books" -H "Content-Type: application/json" -d '{"title": "Book Title", "author": "Author Name", "description": "Description"}'

## Get all books

curl -X GET "http://localhost:8000/books"

## Get a specific book

curl -X GET "http://localhost:8000/books/1"

## Update a book

curl -X PUT "http://localhost:8000/books/1" -H "Content-Type: application/json" -d '{"title": "Updated Title", "author": "Updated Author", "description": "Updated Description"}'

## Delete a book

curl -X DELETE "http://localhost:8000/books/1"
