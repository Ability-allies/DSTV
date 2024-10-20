# Pitch Deck Video:

https://drive.google.com/file/d/1JZdfbWNNJz-NrcFCs9KFQMoktDwenoTW/view?usp=drivesdk


###Down Syndrome Therapy Scheduling Web App - Documentation

##Overview

The Down Syndrome Therapy Scheduling Web App is designed to help parents and caregivers of children with Down syndrome by providing a structured therapy schedule and daily advice. The app focuses on Occupational Therapy (OT), Physiotherapy (PT), and Speech Therapy (ST) to support the development of motor skills, physical strength, and speech capabilities. It also delivers valuable advice tailored to different stages of a child's life, from prenatal care to adulthood.

The web app leverages a Django backend with templating and is designed for ease of use by parents and caregivers to track and manage therapy routines and access useful information based on their child’s developmental stage.

###Key Features

##Daily Therapy Schedules: Automatically generated schedules for Occupational Therapy, Physiotherapy, and Speech Therapy to guide parents through daily routines.

##Calendar View: A visual representation of therapy activities and advice for the current and upcoming days.

##Daily Advice: Advice entries generated and categorized based on different life stages of children with Down syndrome.

##Parent and Child Models: Allows for tracking of multiple children and associates them with their respective parent(s) or caregiver(s).

##Category-based Advice: Structured content divided into different life stages:

Expecting a Baby

New Parents

Preschool and Primary School

Secondary School

Young People

Adults



##Project Structure

down_syndrome_app/
│
├── manage.py
├── requirements.txt
├── down_syndrome/
│   ├── settings.py
│   ├── urls.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── signup.html
│   │   ├── calendar.html
│   │   ├── activity.html
│   │   ├── child.html
│   │   └── journal.html
│   └── static/
│       └── css/
│           └── styles.css
└── scripts/
    └── generate_daily_advice.py

##Core Components

#Models

Parent Model:

Extends Django's built-in User model to store information specific to the parent or caregiver.


Child Model:

Allows parents to add multiple children, with a many-to-many relationship between parents and children.


Therapy and Advice Models:

Therapy models generate schedules for OT, PT, and ST, while the advice model stores daily advice for caregivers. Entries are linked to specific dates for tracking purposes.


#Views

The app includes several views to manage user interaction and content display:

Signup View: Allows parents to register and create accounts.

Calendar View: Displays the therapy schedule and advice for each day.

Activity View: Detailed page for each therapy activity, providing instructions for parents.

Journal View: Enables parents to log notes or track their child’s progress.


#Templates

The app uses Django’s templating system to display HTML pages:

signup.html: Form for new users to create an account.

calendar.html: A visual calendar showing daily therapy tasks and advice.

activity.html: Details of each therapy session for the day.

child.html: A page for managing child profiles.

journal.html: A page for caregivers to log journal entries and track progress.


#API

The project started with an API-based architecture, with endpoints for retrieving therapy schedules and daily advice. It has since transitioned to Django templating to present the content in a web-friendly manner.

#Static Files

The static files directory houses CSS for styling the web pages. Styles can be customized as per the project’s requirements.

##Daily Advice Generation

A script (generate_daily_advice.py) is responsible for generating 365 advice entries, each tailored to specific life stages (prenatal, newborn, preschool, etc.). The AI-generated content ensures continuity and relevance. The advice is stored in the database, and the system assigns it to specific dates so caregivers receive different advice each day.

##Usage

1. Signup
New users (parents or caregivers) can create an account through the signup page.


2. Add Child Profiles
Once logged in, parents can add multiple child profiles, allowing them to manage therapy schedules and advice for each child.


3. View Daily Therapy and Advice
Each day, the calendar displays therapy activities and daily advice tailored to the child's stage in life.


4. Journal
Parents can log their child’s progress in a journal, helping them keep track of improvements and challenges.



Deployment

To deploy the app, follow these steps:

1. Install Dependencies
Ensure you have all required Python packages by running:

pip install -r requirements.txt


2. Database Setup
Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate


3. Run Server
Start the Django development server:

python manage.py runserver


4. Access the Web App
Open a browser and navigate to http://127.0.0.1:8000 to access the app.



##Future Improvements

Mobile App Integration: Build a mobile-friendly interface or dedicated app for easier access to therapy schedules on the go.

Notifications: Add a notification system to remind caregivers of upcoming therapy sessions.

Customization of Therapy Plans: Allow caregivers to customize and modify therapy plans based on their child’s progress.


##Conclusion

This Down Syndrome Therapy Scheduling Web App is designed to be an accessible tool for parents and caregivers, helping them manage therapy schedules and receive advice throughout different stages of a child's life. By leveraging Django’s templating system and AI-generated content, the app provides continuous support and valuable information for the care of children with Down syndrome.





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

This concludes the API documentation for the Down Syndrome Child Care API.

