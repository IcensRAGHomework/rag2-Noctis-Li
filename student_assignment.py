import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def hw02_1(q1_pdf):
    q1_pdf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), q1_pdf)
    loader = PyPDFLoader(file_path=q1_pdf_path)
    docs = loader.load()
    text_splitter = CharacterTextSplitter()
    chunk = text_splitter.split_documents(docs)
    return(chunk[-1])

def hw02_2(q2_pdf):
    q2_pdf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), q2_pdf)
    loader = PyPDFLoader(file_path=q2_pdf_path)
    docs = loader.load()

    full_text = "\n".join([page.page_content for page in docs])

    splits = ["第\\s.+?\\s[章]", "第\\s.+?\\s[條]"]
    text_splitter = RecursiveCharacterTextSplitter(separators=splits, is_separator_regex=True, chunk_overlap=0, chunk_size=10)
    chunks = text_splitter.split_text(full_text)

    i = 0
    for chunk in chunks:
        print(i)
        i += 1
        print(chunk)
    return(len(chunks))