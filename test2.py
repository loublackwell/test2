import streamlit as st
import os

# ===== ABSOLUTE CONFIGURATION =====
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"
os.environ["CHROMA_ALL"] = "YES"
os.environ["CHROMA_SERVER_NO_SQLITE"] = "1"
os.environ["CHROMA_DISABLE_SQLITE"] = "1"  # New nuclear option
# ==================================

def main():
    st.title("Working ChromaDB in Streamlit")
    
    with st.spinner("Initializing..."):
        try:
            # IMPORTANT: Delayed import after environment config
            import chromadb
            from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
            
            # Initialize with explicit DuckDB-only settings
            client = chromadb.Client(
                settings=chromadb.config.Settings(
                    chroma_db_impl="duckdb+parquet",
                    persist_directory=None,  # Disable persistence
                    allow_reset=True
                )
            )
            
            # Test with minimal operations
            collection = client.get_or_create_collection(
                name="streamlit_test",
                embedding_function=DefaultEmbeddingFunction()
            )
            
            collection.add(
                documents=["Finally working in Streamlit Cloud!"],
                ids=["doc1"]
            )
            
            st.success(f"✅ Success! Documents: {collection.count()}")
            st.balloons()
            
        except Exception as e:
            st.error(f"Failed: {str(e)}")
            st.markdown("""
            **Final Resort:**
            1. Create a brand new Streamlit app
            2. Copy this exact code
            3. Use the requirements below
            """)

if __name__ == "__main__":
    main()
