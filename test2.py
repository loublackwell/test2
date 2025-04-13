import streamlit as st
import duckdb
import numpy as np
from sentence_transformers import SentenceTransformer

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def main():
    st.title("DuckDB Vector Search")
    
    # Initialize
    embedder = load_model()
    conn = duckdb.connect(':memory:')
    
    # Create vector table
    conn.execute("""
    CREATE TABLE documents (
        id INTEGER PRIMARY KEY,
        text VARCHAR,
        embedding FLOAT[384]
    )
    """)
    
    # Document upload
    uploaded_file = st.file_uploader("Upload document")
    if uploaded_file:
        text = uploaded_file.read().decode('utf-8')
        embedding = embedder.encode(text).tolist()
        
        conn.execute("""
        INSERT INTO documents VALUES (?, ?, ?)
        """, [1, text, embedding])
        
        st.success("Document stored!")
    
    # Search
    query = st.text_input("Search documents")
    if query:
        query_embed = embedder.encode(query).tolist()
        results = conn.execute("""
        SELECT text, 
               array_cosine_similarity(embedding, ?) as score
        FROM documents
        ORDER BY score DESC
        LIMIT 3
        """, [query_embed]).fetchdf()
        
        st.dataframe(results)

if __name__ == "__main__":
    main()
