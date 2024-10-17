# Down Syndrome Child Care API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Base URL](#base-url)
3. [Authentication](#authentication)
4. [Endpoints](#endpoints)
   - [User Management](#user-management)
     - [User Registration](#user-registration)
     - [User Login](#user-login)
     - [List Users](#list-users)
     - [Retrieve User](#retrieve-user)
     - [Update User](#update-user)
     - [Delete User](#delete-user)
   - [Child Management](#child-management)
     - [List Children](#list-children)
     - [Create Child](#create-child)
     - [Retrieve Child](#retrieve-child)
     - [Update Child](#update-child)
     - [Delete Child](#delete-child)
   - [Advice Management](#advice-management)
     - [List Daily Advice](#list-daily-advice)
     - [Retrieve Advice](#retrieve-advice)
5. [Models](#models)
   - [User](#user)
   - [Child](#child)
   - [Advice](#advice)
6. [Error Handling](#error-handling)
   - [Common Error Codes](#common-error-codes)
   - [Error Response Format](#error-response-format)

## Introduction
This document provides detailed information about the Down Syndrome Child Care API. It covers authentication, available endpoints, request/response formats, and error handling.

## Base URL
All URLs referenced in the documentation have the following base:
http://localhost:8000/api/

## Authentication
The API uses Token-based authentication. Include the token in the Authorization header for all authenticated requests:

Authorization: Bearer <token>
To obtain a token, use the login endpoint.

## Endpoints

### User Management

#### User Registration
- **URL:** `/signup/`
- **Method:** `POST`
- **Auth required:** No

##### Request Body
| Field       | Type   | Required | Description                    |
|-------------|--------|----------|--------------------------------|
| username    | string | Yes      | User's username                |
| password    | string | Yes      | User's password                |
| email       | string | Yes      | User's email address           |
| first_name  | string | Yes      | User's first name             |
| last_name   | string | Yes      | User's last name              |

##### Success Response
- **Code:** `201 CREATED`
- **Content:**
```json
{
  "user": {
    "id": 1,
    "username": "example_user",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "token": "your-auth-token"
}

User Login
URL: /login/
Method: POST
Auth required: No

Request Body
Field	Type	Required	Description
username	string	Yes	User's username
password	string	Yes	User's password

Success Response
Code: 200 OK
Content:
{
  "token": "Bearer your-auth-token",
  "user_id": 1,
  "email": "user@example.com"
}
List Users
URL: /users/
Method: GET
Auth required: Yes (Admin only)
Success Response
Code: 200 OK
Content:
[
  {
    "id": 1,
    "username": "example_user",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  // ... more users
]
Retrieve User
URL: /users/<id>/
Method: GET
Auth required: Yes (Admin only)
Success Response
Code: 200 OK
Content:
{
  "id": 1,
  "username": "example_user",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
Update User
URL: /users/<id>/
Method: PUT
Auth required: Yes (Admin only)
Request Body
Same as User Registration, but all fields are optional.
Success Response
Code: 200 OK
Content: Updated user object
Delete User
URL: /users/<id>/
Method: DELETE
Auth required: Yes (Admin only)
Success Response
Code: 204 NO CONTENT
Child Management
List Children
URL: /children/
Method: GET
Auth required: Yes
Success Response
Code: 200 OK
Content:
[
  {
    "id": 1,
    "name": "Child A",
    "age": 3,
    "parent_id": 1
  },
  // ... more children
]
Create Child
URL: /children/
Method: POST
Auth required: Yes

Request Body
Field	Type	Required	Description
name	string	Yes	Child's name
age	integer	Yes	Child's age
parent_id	integer	Yes	ID of the associated parent

Success Response
Code: 201 CREATED
Content: Created child object
Retrieve Child
URL: /children/<id>/
Method: GET
Auth required: Yes
Success Response
Code: 200 OK
Content: Child object
Update Child
URL: /children/<id>/
Method: PUT
Auth required: Yes
Request Body
Same as Create Child, but all fields are optional.
Success Response
Code: 200 OK
Content: Updated child object
Delete Child
URL: /children/<id>/
Method: DELETE
Auth required: Yes
Success Response
Code: 204 NO CONTENT
Advice Management
List Daily Advice
URL: /advice/
Method: GET
Auth required: Yes
Success Response
Code: 200 OK
Content:
[
  {
    "id": 1,
    "date": "2024-10-01",
    "advice": "Daily advice for parents."
  },
  // ... more advice
]
Retrieve Advice
URL: /advice/<id>/
Method: GET
Auth required: Yes
Success Response
Code: 200 OK
Content: Advice object
Models
User
id: Integer
username: String
email: String
first_name: String
last_name: String
Child
id: Integer
name: String
age: Integer
parent_id: ForeignKey(User)
Advice
id: Integer
date: Date
advice: Text
Error Handling
The API uses standard HTTP response codes to indicate the success or failure of requests. In case of errors, the response will include a JSON object with more details about the error.

Common Error Codes
400 Bad Request: The request was invalid or cannot be served.
401 Unauthorized: The request requires authentication.
403 Forbidden: The server understood the request but refuses to authorize it.
404 Not Found: The requested resource could not be found.
500 Internal Server Error: The server encountered an unexpected condition which prevented it from fulfilling the request.

Error Response Format
{
  "detail": "Error message describing the issue"
}
For validation errors, the response may include field-specific error messages:
{
  "field_name": [
    "Error message for this field"
  ]
}

This concludes the API documentation for the Down Syndrome Child Care API. Happy coding!

