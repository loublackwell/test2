import streamlit as st
import duckdb
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize embedding model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def main():
    st.title("Vector Search with DuckDB")
    
    # Initialize components
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
    
    # File upload
    uploaded_file = st.file_uploader("Upload documents", type=['txt', 'pdf'])
    if uploaded_file:
        text = uploaded_file.read().decode('utf-8')
        
        # Generate embedding
        embedding = embedder.encode(text)
        
        # Store in DuckDB
        conn.execute("""
        INSERT INTO documents 
        VALUES (?, ?, ?)
        """, [1, text, embedding.tolist()])
        
        st.success("Document stored!")
    
    # Search interface
    query = st.text_input("Search documents")
    if query:
        # Embed query
        query_embedding = embedder.encode(query)
        
        # Vector search
        results = conn.execute("""
        SELECT id, text, 
               array_cosine_similarity(embedding, ?) as similarity
        FROM documents
        ORDER BY similarity DESC
        LIMIT 3
        """, [query_embedding.tolist()]).fetchdf()
        
        st.dataframe(results)

if __name__ == "__main__":
    main()
