from langchain_community.document_loaders import PyPDFLoader
import os


#File Uploader

#For Single File 

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents= loader.load()
    return documents

#For all Files

def load_all_pdfs(folder_path):
    all_documents = {}

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            all_documents[file] = documents

    return all_documents