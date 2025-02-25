import os
import csv
import json
import pandas as pd
from PIL import Image
import PyPDF2

# Step 1 - Understanding the Data Directory
def list_files(data_dir):
    try:
        files = os.listdir(data_dir)
        print("Files in directory:")
        for file in files:
            print(file)
        return files
    except FileNotFoundError:
        print(f"The directory {data_dir} does not exist.")
        return []

# Step 2 - Opening and Reading Files
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print("First 5 lines of the text file:")
            for line in lines[:5]:
                print(line.strip())
    except Exception as e:
        print(f"Error reading text file {file_path}: {e}")

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        print("First 3 rows of the CSV file:")
        print(df.head(3))
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("Key-value pairs in the JSON file:")
            for key, value in data.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Error reading JSON file {file_path}: {e}")

def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        print("First 3 rows of the Excel file:")
        print(df.head(3))
    except Exception as e:
        print(f"Error reading Excel file {file_path}: {e}")

def display_image(file_path):
    try:
        image = Image.open(file_path)
        image.show()
    except Exception as e:
        print(f"Error displaying image {file_path}: {e}")

def read_pdf_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if len(reader.pages) > 0:
                first_page = reader.pages[0]
                text = first_page.extract_text()
                if text:
                    print("First few lines of the PDF file:")
                    print(text.split('\n')[:5])
                else:
                    print("No text found on the first page of the PDF file.")
            else:
                print("The PDF file is empty.")
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {e}")

def main():
    data_dir = "dataset"
    files = list_files(data_dir)

    for file in files:
        file_path = os.path.join(data_dir, file)
        if file.endswith('.txt'):
            read_text_file(file_path)
        elif file.endswith('.csv'):
            read_csv_file(file_path)
        elif file.endswith('.json'):
            read_json_file(file_path)
        elif file.endswith('.xlsx'):
            read_excel_file(file_path)
        elif file.endswith('.jpg'):
            display_image(file_path)
        elif file.endswith('.pdf'):
            read_pdf_file(file_path)

if __name__ == "__main__":
    main()