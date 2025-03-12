# CRUD Product API

This is a Django REST Framework (DRF) based API that allows users to:
- Register and authenticate
- Create, read, update, and delete (CRUD) products
- Comment on products
- Search and filter products
-

## Features

### User Registration
- Users can register using a username, password, and email.

### Product Management
- Users can create and list products.
- Products can be searched and filtered by name or ID.
- Authenticated users can comment on products.
- Users can update or delete their own comments.

## API Endpoints

### User Authentication
- `POST /api/register/` - Register a new user.
- `POST /api/token/` - Obtain JWT token.
- `POST /api/token/refresh/` - Refresh JWT token.

### Product Endpoints
- `GET /api/products/` - List all products (supports search & filtering by name or ID).
- `POST /api/products/` - Create a new product (requires authentication).
- `GET /api/products/{id}/` - Retrieve a specific product.
- `PUT /api/products/{id}/` - Update a product (requires authentication).
- `DELETE /api/products/{id}/` - Delete a product (requires authentication).

### Comment Endpoints
- `POST /api/products/{product_id}/comments/` - Add a comment to a product.
- `PUT /api/comments/{id}/` - Update a comment (only by the author).
- `DELETE /api/comments/{id}/` - Delete a comment (only by the author).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/afnanshihab8/crudproject.git
   cd crudproject
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Use Postman or cURL to interact with the API.
- Authenticate users to access protected endpoints.

## cURL Tests

### Register a New User
```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass", "email": "test@example.com"}'
```

### Obtain JWT Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}'
```

### Create a Product (Authenticated)
```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"name": "Laptop", "description": "Gaming Laptop", "price": "2000.00"}'
```

### Search for a Product
```bash
curl -X GET "http://127.0.0.1:8000/api/products/?search=laptop"
```

### Add a Comment to a Product
```bash
curl -X POST http://127.0.0.1:8000/api/products/1/comments/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"content": "This is an awesome product!"}'
```

### Update a Comment 
```bash
curl -X PUT http://127.0.0.1:8000/api/comments/1/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"content": "Updated comment!"}'
```

### Delete a Comment 
```bash
curl -X DELETE http://127.0.0.1:8000/api/comments/1/ \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
