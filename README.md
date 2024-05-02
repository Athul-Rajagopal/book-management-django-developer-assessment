# Book management

## Description

This project is done as part of the interview process. The task is to create APIs for managing books, users, and reading lists. Here is the short description of task. 
1. User Management:
    -Users should be able to register, log in, and manage their profiles.
    -Each user should have a unique username and email address.
2. Book Management:
    -Users should be able to create, remove, and upload books.
    -All users should be able to access all the books.
    -Each book should have a title, author(s), genre, publication date, and an optional description.
3. Reading Lists:
    -Users should be able to create and manage reading lists.
    -Reading lists should allow users to organise their books in their preferred order.
4. Interactions:
    -Users should be able to add books to their reading lists and remove them.
5. Error Handling:
    -Handle potential errors gracefully and provide informative error responses to users.

Utilized JWT token authentication and authorization for managing user sessions.


## Installation

1. Clone the repository to your local machine:
git clone https://github.com/Athul-Rajagopal/book-management-django-developer-assessment.git

2. Navigate to the project directory:
cd <project-directory>

3. Install the required dependencies:
```pip install -r requirements.txt```

4. Apply migrations:
```python manage.py makemigration```
```python manage.py migrate```

5. Run the development server:
```python manage.py runserver```


# API Documentation

## 1. User Management

### 1. Register User

- **Description**: Register a new user.
- **Method**: POST
- **URL**: `/register/`

#### Request body

| Parameter Name    | Description                      | Type & Length    |
|--------------------|---------------------------------|------------------|
| username           | Unique username for the user    | string           |
| email              | Unique email address for the user | string         |
| password           | User's password                  | string           |
| confirm-password   | Re-entered password              | string           |

**Sample input:**
```json
{
    "username": "example_user",
    "email": "user@example.com",
    "password": "example_password",
    "confirm-password": "example_password"
}
```

**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|201        | Created 
|400             |Bad request | 

**sample response for success**
```json
{
    "message": "User registered successfully"
}
```
**Sample response for error (400 Bad Request):**
```json
{
    "message": "Username or email already exists, or password does not match"
}
```

### 2. User Login
- **Description**: Login a user and get an authentication token..
- **Authorization**: Token authentication required
- **Method**: POST
- **URL**: `/login/`

#### Request body

| Parameter Name    | Description                      | Type & Length    |
|--------------------|---------------------------------|------------------|
| username           |user's username    | string           |
| password            | user's password | string         |

**Sample input:**
```json
{
    "username": "example_user",
    "password": "example_password"
}
```
**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|401             |Unauthorized | 

**sample response for success**
```json
{
    "message": "Login successful",
"access": "<access token>",
"refresh": "<refresh token>"}
```
**Sample response for error (Unauthorized ):**
```json
{"message":" Invalid credentials."}
```

### 3. User profile

- **Description**: View or update user profile information
- **Authorization**: Token authentication required
- **Method**: GET
- **URL**: `/profile/`
- **Method**: PUT
- **URL**: `/profile/`

#### Request body
- **PUT**:

| Parameter Name    | Description                      | Type & Length    |
|--------------------|---------------------------------|------------------|
| username           |Updated username    | string           |
| email          |Updated email | string         |

**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|400            |Bad request| 

**sample response for success**
-**GET**
```json
{
    "id": 1,
    "username": "example_user",
    "email": "user@example.com"
}

```
-**PUT**
```json
 {"message" : "profile updated successfully" }
```

**Sample response for error (Bad request ):**
```json
{"message" : "Validation error"}
```

### 3. User logout

- **Description**: Logout a user
- **Method**: POST
- **URL**: `/logout/`

**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK

**sample response for success**
```json
{"message" : "Logged out successfully" }
```

## 2. Book Management

### 1. Book List

- **Description**: List all books.
- **Authorization**: Token authentication required
- **Method**: GET
- **URL**: `/books/`

**Response:**
- **Array of book objects**

**sample response for success**
```json
[
    {
        "id": 1,
        "title": "Sample Book 1",
        "authors": "Author 1",
        "genre": "Fiction",
        "publication_date": "2022-01-01",
        "description": "This is a sample book."
    },
    {
        "id": 2,
        "title": "Sample Book 2",
        "authors": "Author 2",
        "genre": "self help",
        "publication_date": "2023-01-01",
        "description": null
    }
]
```
### 2. Create Book

- **Description**: Create a new book.
- **Authorization**: Token authentication required
- **Method**: POST
- **URL**: `/books/`

#### Request body

| Parameter Name    | Description                      | Type & Length    |
|--------------------|---------------------------------|------------------|
| title          |title of book | string           |
|authors    | author’s name | string         |
| genre           |Genre of book    | string           |
| publication_date            | date of publication | string         |
| description           |Short description about book(if any)    | string           |

**Sample input:**
```json
{
    "title": "Example Book",
    "authors": "John Doe",
    "genre": "Fiction",
    "publication_date": "2024-01-01",
    "description": "An example book."
}
```
**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|400            |Bad request| 

**sample response for success**
```json
{"message" : "Book created successfully" }
```
**Sample response for error (Bad request ):**
```json
{"message" : "Validation error"}
```

### 3. Retrieve Book

- **Description**: Retrieve details of a specific book.
- **Authorization**: Token authentication required
- **Method**: GET
- **URL**: `/books/<book_id>/`

**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|404            |Not found| 

**sample response for success**
```json
{
    "title": "Example Book",
    "authors": "John Doe",
    "genre": "Fiction",
    "publication_date": "2024-01-01",
    "description": "An example book."
}

```
**Sample response for error (Not found ):**
```json
{"message" :"‘not found’"}
```


### 4. Delete Book
- **Description**: Delete a specific book.
- **Authorization**: Token authentication required
- **Method**: DELETE
- **URL**: `/books/<book_id>/`

**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|204        | No content
|404            |Not found| 


## 3. Reading List Management

### 1. List reading Lists

- **Description**: List all reading lists.
- **Authorization**: Token authentication required
- **Method**: GET
- **URL**: `/reading-lists/`

**Response:**
- **Array of reading list objects**

**sample response for success**
```json
[
    {
        "id": 1,
        "name": "Sample Reading List",
        "books": [
            {
                "id": 1,
                "title": "Sample Book 1",
                "authors": "Author 1",
                "genre": "Fiction",
                "publication_date": "2022-01-01",
                "description": "This is a sample book.",
                "order": 1
            },
            {
                "id": 2,
                "title": "Sample Book 2",
                "authors": "Author 2",
                "genre": "self help",
                "publication_date": "2023-01-01",
                "description": null,
                "order": 2
            }
        ]
    },
 {
        "id": 2,
        "name": "My Reading List",
        "books": [
            {
                "id": 1,
                "title": "Sample Book 1",
                "authors": "Author 1",
                "genre": "Fiction",
                "publication_date": "2022-01-01",
                "description": "This is a sample book.",
                "order": 1
            },
            {
                "id": 2,
                "title": "Sample Book 2",
                "authors": "Author 2",
                "genre": "self help",
                "publication_date": "2023-01-01",
                "description": null,
                "order": 2
            }
        ]
    }
]
```

### 2. Create Reading List

- **Description**: Create a new reading list.
- **Authorization**: Token authentication required
- **Method**: POST
- **URL**: `/create-reading-list/`

#### Request body

| Parameter Name    | Description                      | Type & Length    |
|--------------------|---------------------------------|------------------|
| name          |Name of Reading list | string           |
|books    |Array of book objects | Array         |
| title           |title of books    | string           |
| order          |Arrangement order of book in list    | number           |

**Sample input:**
```json
{
    "name": "My Reading List",
    "books": [
        {
            "title": " Book 1 title",
            "order": 1
        },
        {
            "title": "Book 2 title",
            "order": 2
        }
    ]
}
```
**Response:**
| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|404            |Not found| 

**sample response for success**
```json
{"message" : "Reading list created successfully"}
```
**Sample response for error (Not found ):**
```json
 {"message" :"Object not found"}
```


### 3. Retrieve Reading List

- **Description**: Retrieve a specific reading list.
- **Authorization**: Token authentication required
- **Method**: GET
- **URL**: `/reading-lists/<reading_list_id>/`

**Response:**

| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|404            |Not found| 

**sample response for success**
```json
 {
        "id": 1,
        "name": "Sample Reading List",
        "books": [
            {
                "id": 1,
                "title": "Sample Book 1",
                "authors": "Author 1",
                "genre": "Fiction",
                "publication_date": "2022-01-01",
                "description": "This is a sample book.",
                "order": 1
            },
            {
                "id": 2,
                "title": "Sample Book 2",
                "authors": "Author 2",
                "genre": "self help",
                "publication_date": "2023-01-01",
                "description": null,
                "order": 2
            }
        ]
    }
```
**Sample response for error (Not found ):**
```json
 {"message" :"Object not found"}
```

### 4. Update Reading List
- **Description**: Update details of a specific reading list.
- **Authorization**: Token authentication required
- **Method**: PUT
- **URL**: `/reading-lists/<reading_list_id>/`

#### Request body

| Parameter Name    | Description                      | Type & Length    |
|--------------------|---------------------------------|------------------|
| name          |Name of Reading list | string           |
|books    |Array of book objects | Array         |
| title           |title of books    | string           |
| order          |Arrangement order of book in list    | number           |

**Sample input:**
```json
{
    "name": "My Reading List",
    "books": [
        {
            "title": " Book 1 title",
            "order": 1
        },
        {
            "title": "Book 2 title",
            "order": 2
        }
    ]
}
```
**Response:**

| status code    | Description                      
|--------------------|---------------------------------|
|200        | OK
|400            |Bad request| 

**sample response for success**
```json
{"message" : "Reading list updated successfully"}
```
**Sample response for error (Bad request ):**
```json
 {"message ":"Validation error."}
```


### 5. Delete Reading List
- **Description**: Delete a specific reading list.
- **Authorization**: Token authentication required
- **Method**: DELETE
- **URL**: `/reading-lists/<reading_list_id>/`

| status code    | Description                      
|--------------------|---------------------------------|
|204        | No content
