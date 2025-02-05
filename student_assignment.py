import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    q1_pdf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), q1_pdf)
    print(q1_pdf_path)
    loader = PyPDFLoader(file_path=q1_pdf_path)
    docs = loader.load()
    text_splitter = CharacterTextSplitter()
    chunk = text_splitter.split_documents(docs)
    print(chunk[-1])
    return(chunk[-1])

def hw02_2(q2_pdf):
    q2_pdf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), q2_pdf)
