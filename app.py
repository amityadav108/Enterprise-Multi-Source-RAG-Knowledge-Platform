import pickle
import faiss
from fastapi import FastAPI
from pydantic import BaseModel

# Load metadata
with open("data/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# Load vectorizer
with open("data/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load FAISS index
index = faiss.read_index("data/faiss_index.bin")

# Create FastAPI app
app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


def retrieve_context(question, k=3):

    query_vector = vectorizer.transform([question])
    query_vector = query_vector.toarray().astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []

    for idx in indices[0]:
        results.append({
            "source": metadata[idx]["source"],
            "text": metadata[idx]["text"]
        })

    return results


def generate_answer(question):

    results = retrieve_context(question)

    return {
        "question": question,
        "answer": results[0]["text"],
        "sources": [results[0]["source"]]
    }


@app.get("/")
def home():

    return {
        "message": "Enterprise Multi-Source RAG API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    return generate_answer(request.question)


from fastapi.responses import JSONResponse

@app.get("/hybridaction/zybTrackerStatisticsAction")
def ignore_tracker():
    return JSONResponse({"status": "ignored"})