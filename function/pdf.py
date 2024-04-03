import os
from utils.extract import extract_text_from_pdf

class Pdf():
    def __init__(self):
        self.pdf_directory = './content/pdf_files'
        os.makedirs(self.pdf_directory, exist_ok=True)

    def get_summary(self, directory):
        return extract_text_from_pdf(directory)

    def get_pdf_files(self):
        return [self.pdf_directory + '/' + file for file in os.listdir(self.pdf_directory) if file.endswith(".pdf")]