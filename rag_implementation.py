import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline, set_seed
import streamlit as st
import transformers
import requests
from sentence_transformers import SentenceTransformer
import numpy
import faiss
from pyngrok import ngrok


API_TOKEN = "....your huggingface api token....."

#loading the data we saved
class TextLoader:
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding

    def load(self):
        with open(self.file_path, 'r', encoding=self.encoding) as file:
            data = file.read()
        return data.split("\n\n")

file_path = "....your file path......"
loader = TextLoader(file_path=file_path, encoding="utf-8")
data = loader.load()

#intializing the embeddings of data
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedding_model.encode(data)
doc_embeddings =  numpy.array(doc_embeddings).astype('float32')

#faiss index for semantic search

assert doc_embeddings.ndim == 2, "Embeddings should be a 2D array"

embedding_dimension = doc_embeddings.shape[1]
index_flat = faiss.IndexFlatL2(embedding_dimension)
doc_embeddings = numpy.array(doc_embeddings).astype("float32")
index_flat.add(doc_embeddings)

#intializing the RAG(retrieving the relevent documents from data)

def retrieve_relevent_docs(input, num_docs = 5):
    input_embedding = embedding_model.encode([input])
    query_embedding = numpy.array(input_embedding).astype("float32")
    distances, indices = index_flat.search(query_embedding, num_docs)

    retrieved_docs = [data[i] for i in indices[0]]
    print("Retrieved Documents:", retrieved_docs)
    return retrieved_docs


#integrating into the streamlit to interact with answers

st.title("talk to paul graham")


#getting the access of the model from huggingface via serverless api inference.

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "....add hugging face model  url for any model you want to utilize....."

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

#integrating into the streamlit

if API_TOKEN:
    question = st.text_input("what do you want to ask ?")
    if question:
        retrieved_docs = retrieve_relevant_docs(question)
        context = " ".join(retrieved_docs)
        payload = {"inputs": context}
        answer = query(payload)


        st.write(f"**Question:** {question}")
        st.write(f"**Context:** {context}")
        if 'summary_text' in answer:
            st.write(f"**Answer:** {answer['summary_text']}")
        else:
            st.write(f"**Error:** {answer.get('error', 'Unknown error')}")

#hosting all of this thing into the ngrok with streamlit.

ngrok.set_auth_token("....your ngrok auth token to host this into temperarory website....")

public_url = ngrok.connect(8501)
print(f"Streamlit app is live at: {public_url}")

!streamlit run paulg.py >/dev/null
