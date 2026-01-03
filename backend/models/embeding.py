from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
EMBEDDING_DIM = 384

def embed(text: str):
    return embedding_model.encode(text).astype("float32")
