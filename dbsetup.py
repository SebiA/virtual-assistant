from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from utils import get_embeddings
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file_name', action="store", dest='file_name', default="")
args = parser.parse_args()


def create_db(file_name: str=""):
    loader = TextLoader(f"./content/{file_name}", encoding='utf-8')
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100, chunk_overlap=20)
    docs = text_splitter.split_documents(documents)
    hf = get_embeddings()
    db = FAISS.from_documents(docs, hf)
    db.save_local("data")


if __name__=="__main__":
    create_db(file_name=args.file_name)

