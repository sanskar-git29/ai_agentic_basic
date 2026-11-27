import os
import json

import numpy
from openai import OpenAI
from dotenv import load_dotenv

from utility.utility import log

load_dotenv() #by default looks for .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
VECTOR_STORE_FILE = os.getenv("VECTOR_STORE_FILE")

def get_embedding(text):
    response = client.embeddings.create(
        model=os.getenv("EMBEDDING_MODEL"),
        input=text,
    )
    return response.data[0].embedding

def cosine_similarity(A, B):
    dot_prod = numpy.dot(A, B)
    norm_a = numpy.linalg.norm(A)
    norm_b = numpy.linalg.norm(B)
    return dot_prod / (norm_a * norm_b)

def chunks_document(document):
    chunks=[]
    chunk_id=0
    for part in document["text"].split("\n\n"):
        part=part.strip()
        if part:
            chunks.append({
                "source":document["source"],
                "chunk_id":chunk_id,
                "text":part
            })
            chunk_id+=1

    return chunks

def create_chunks(folder_name):
    documents = load_documents(folder_name)
    chunks = []

    for document in documents:
        chunks.extend(chunks_document(document))

    return chunks

def load_documents(folder_name):
  

    documents=[];
    for name in os.listdir(folder_name):

        if not name.endswith(".txt"):
            continue
        path=os.path.join(folder_name,name) 
        
        with open(path,"r",encoding="UTF-8")as f:
            
            documents.append({
                "source":name,
                "text":f.read(),   
            })

    return documents

def add_embedding(chunks):
    for chunk in chunks:
        vector=get_embedding(chunk["text"])
        chunk["vector"]=vector
    return chunks

def save_vector_store(chunks):
    with open(VECTOR_STORE_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=4)

def load_vector_store():
    with open(VECTOR_STORE_FILE, "r", encoding="utf-8") as f:
        return json.load(f) #returns the chunks

def load_chunks(FOLDER_NAME):
    if os.path.exists(VECTOR_STORE_FILE):
        chunks = load_vector_store()
        log(f"Loaded {len(chunks)} chunks from the {VECTOR_STORE_FILE}")
    else:
        chunks = create_chunks(FOLDER_NAME)
        chunks = add_embedding(chunks)
        save_vector_store(chunks)
        log(f"Created and embedded {len(chunks)} chunks and saved to {VECTOR_STORE_FILE}")

    return chunks

def search_query( query,document,top_k=3):
    query_embedding=get_embedding(query)
    res=[]

    for doc in document:
        score=cosine_similarity(query_embedding,doc["vector"])

        res.append({
            "source": doc["source"],
            "chunk_id": doc["chunk_id"],
            "text": doc["text"],
            "score": score
        })
    res.sort( key=lambda rec:rec["score"] ,reverse=True)

    return ( res[:top_k])






















