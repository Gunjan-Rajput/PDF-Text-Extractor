from fastapi import FastAPI, Request, UploadFile, File
import json
import PyPDF2
import pymongo
from loguru import logger
from io import BytesIO
import requests
import os

app = FastAPI()

# MongoDB setup
mongo_uri = os.getenv("MONGO_URI", "your_default_mongodb_uri")
client = pymongo.MongoClient(mongo_uri)
db = client.get_database("your_database")
collection = db.get_collection("your_collection")

@app.post("/process_pdf_url/")
async def process_pdf_url(request: Request):
    message = await request.json()
    logger.info(f"Received message: {message}")

    # Assuming the message contains the URL of the PDF file
    pdf_url = message.get("pdf_url")

    # Download and process the PDF
    return await process_pdf(pdf_url)

@app.post("/process_pdf_file/")
async def process_pdf_file(file: UploadFile = File(...)):
    # Save file locally for processing
    contents = await file.read()
    with open(file.filename, 'wb') as f:
        f.write(contents)
    
    # Process saved file
    return await process_pdf(file.filename, is_local_file=True)

async def process_pdf(pdf_source, is_local_file=False):
    # Process the PDF from URL or local file
    file = BytesIO(requests.get(pdf_source).content) if not is_local_file else open(pdf_source, 'rb')

    # Extract text from PDF
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()
    
    if is_local_file:
        file.close()

    # Save to MongoDB
    pdf_document = {"source": pdf_source, "text": text}
    collection.insert_one(pdf_document)

    return {"status": "Processing completed"}