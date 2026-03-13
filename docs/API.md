# API Reference

This document provides a comprehensive overview of all the API endpoints available in the ShuttleMatch platform.

## Authentication

### Register a New User

- **Endpoint**: `/api/v1/auth/register`
- **Method**: POST
- **Description**: Register a new user
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string",
    "role": "string"
  }
  ```
- **Response Schema**:
  ```json
  {
    "id": "UUID",
    "email": "string",
    "role": "string"
  }
  ```

### Login User

- **Endpoint**: `/api/v1/auth/login`
- **Method**: POST
- **Description**: Login user and return JWT
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response Schema**:
  ```json
  {
    "access_token": "string",
    "refresh_token": "string"
  }
  ```

### Refresh JWT Token

- **Endpoint**: `/api/v1/auth/refresh`
- **Method**: POST
- **Description**: Refresh JWT token
- **Request Body**:
  ```json
  {
    "refresh_token": "string"
  }
  ```
- **Response Schema**:
  ```json
  {
    "access_token": "string"
  }
  ```

### Logout User

- **Endpoint**: `/api/v1/auth/logout`
- **Method**: POST
- **Description**: Logout user and invalidate token
- **Request Body**: `{}`
- **Response Schema**:
  ```json
  {
    "message": "string"
  }
  ```

## Tournaments

### Create a New Tournament

- **Endpoint**: `/api/v1/tournaments`
- **Method**: POST
- **Description**: Create a new tournament
- **Request Body**:
  ```json
  {
    "name": "string",
    "location": "string",
    "date": "string"
  }
  ```
- **Response Schema**:
  ```json
  {
    "id": "UUID",
    "name": "string",
    "location": "string",
    "date": "string"
  }
  ```

### List All Tournaments

- **Endpoint**: `/api/v1/tournaments`
- **Method**: GET
- **Description**: List all tournaments
- **Response Schema**:
  ```json
  [
    {
      "id": "UUID",
      "name": "string",
      "location": "string",
      "date": "string"
    }
  ]
  ```
- **Query Parameters**: `page`, `limit`

### Get Tournament Details

- **Endpoint**: `/api/v1/tournaments/{tournament_id}`
- **Method**: GET
- **Description**: Get tournament details
- **Response Schema**:
  ```json
  {
    "id": "UUID",
    "name": "string",
    "location": "string",
    "date": "string",
    "matches": "array"
  }
  ```

[...additional endpoints...]