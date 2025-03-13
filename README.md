# CRUD Product API

This is a Django REST Framework (DRF) based API that allows users to:
- Register and authenticate
- Create, read, update, and delete (CRUD) products
- Comment on products
- Search and filter products


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
   git clone https://github.com/afnanshihab8/BackendAPI.git
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

- Use Postman or Httpie to interact with the API.
- Authenticate users to access protected endpoints.

## Using HTTPie to Test the API

### Obtain Access Token
Before making authenticated requests, obtain an access token using your credentials:
```sh
http POST http://127.0.0.1:8000/api/token/ username="your_username" password="your_password"
```
Response:
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

### Use Access Token in Requests
Include the access token in the `Authorization` header:
```sh
http GET http://127.0.0.1:8000/api/products/ "Authorization: Bearer your_access_token"
```

### Refresh Access Token
```sh
http POST http://127.0.0.1:8000/api/token/refresh/ refresh="your_refresh_token"
```

## CRUD Operations

### Create a Product (Authenticated)
```sh
http POST http://127.0.0.1:8000/api/products/ "Authorization: Bearer your_access_token" name="Nikon Cool Pix" description="Digital Camera" price:=6000
```

### Get All Products (Public)
```sh
http GET http://127.0.0.1:8000/api/products/
```

### Update a Product (Authenticated)
```sh
http PUT http://127.0.0.1:8000/api/products/1/ "Authorization: Bearer your_access_token" name="Updated Product" description="Updated Description" price:=7000
```

### Delete a Product (Authenticated)
```sh
http DELETE http://127.0.0.1:8000/api/products/1/ "Authorization: Bearer your_access_token"
```

## Comments

### Add a Comment (Authenticated)
```sh
http POST http://127.0.0.1:8000/api/products/1/comments/ "Authorization: Bearer your_access_token" text="Amazinf product!"
```

### Get All Comments (Public)
```sh
http GET http://127.0.0.1:8000/api/products/1/comments/
```

### Update a Comment (Authenticated)
```sh
http PUT http://127.0.0.1:8000/api/comments/1/ "Authorization: Bearer your_access_token" text="Updated comment"
```

### Delete a Comment (Authenticated)
```sh
http DELETE http://127.0.0.1:8000/api/comments/1/ "Authorization: Bearer your_access_token"
```

## Additional Features

### Pagination (Public)
```sh
http GET http://127.0.0.1:8000/api/products/?page=1
```

### Search (Public)
```sh
http GET http://127.0.0.1:8000/api/products/?search=Cool
```




