import streamlit as st
import os

# Critical configuration - MUST come before chromadb import
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"  # Completely bypasses SQLite
os.environ["CHROMA_ALL"] = "YES"  # Enable all workarounds

def main():
    st.title("ChromaDB in Streamlit Cloud")
    
    with st.spinner("Initializing ChromaDB..."):
        try:
            import chromadb
            
            # Initialize client
            client = chromadb.Client()
            
            # Test functionality
            collection = client.create_collection("test_docs")
            collection.add(
                documents=["This is a test document"],
                ids=["doc1"]
            )
            
            st.success("✅ ChromaDB working perfectly!")
            st.write(f"Documents in collection: {collection.count()}")
            
        except Exception as e:
            st.error(f"Failed to initialize ChromaDB: {str(e)}")
            st.markdown("""
            **Troubleshooting Steps:**
            1. Ensure `requirements.txt` includes `duckdb>=0.9.0`
            2. Try clearing Streamlit cache (Settings → Clear Cache)
            3. Contact Streamlit support if issue persists
            """)

if __name__ == "__main__":
    main()
