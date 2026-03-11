import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_classic.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
PDF_PATH = Path("data/transformers.pdf")
load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("Missing GOOGLE_API_KEY. Set it in your environment or .env file.")
if not PDF_PATH.exists():
    raise FileNotFoundError(f"Missing PDF file at '{PDF_PATH}'.")
loader = PyPDFLoader(str(PDF_PATH))
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(documents)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="db")
retriever = vectorstore.as_retriever()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
print("ask your questions. type exit or quit to stop.")
while True:
    try:
        query = input("Ask: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nBad input.")
        break
    if query.lower() in {"exit", "quit"}:
        print("Exited successfully.")
        break
    if not query:
        continue
    result = qa.run(query)
    print(result)
