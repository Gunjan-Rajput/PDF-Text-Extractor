# PDF Text Extractor

This project is a PDF Text Extractor API built with FastAPI and MongoDB. It allows users to upload PDF files, extract text from them, and store the extracted text in a MongoDB database.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features
- Upload PDF files.
- Extract text content from PDF files.
- Store extracted text in MongoDB.
- Retrieve extracted text by PDF ID.

## Requirements
- Python 3.8+
- MongoDB
- Pipenv (optional, for virtual environment management)

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/pdf-text-extractor.git
    cd pdf-text-extractor
    ```

2. **Set up a virtual environment:**
    Using `pipenv` (recommended):
    ```bash
    pipenv install
    pipenv shell
    ```

    Using `venv` and `pip`:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Install MongoDB:**
    Follow the instructions on the [MongoDB installation page](https://docs.mongodb.com/manual/installation/) to install MongoDB on your system.

## Configuration
Create a `.env` file in the project root directory with the following content:

MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=pdf_text_extractor


## Usage
1. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

2. **Access the API documentation:**
    Open your web browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## API Endpoints
- **`POST /upload`**: Upload a PDF file.
  - Request: Multipart/form-data with file field.
  - Response: JSON with PDF ID and extracted text.

- **`GET /pdf/{pdf_id}`**: Retrieve extracted text by PDF ID.
  - Request: PDF ID as a path parameter.
  - Response: JSON with PDF ID and extracted text.

## Running Tests
1. **Install test dependencies:**
    ```bash
    pip install -r requirements-test.txt
    ```

2. **Run the tests:**
    ```bash
    pytest
    ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

