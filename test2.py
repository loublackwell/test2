import streamlit as st
import os

# ===== CRITICAL CONFIGURATION =====
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"
os.environ["CHROMA_ALL"] = "YES"
os.environ["CHROMA_SERVER_NO_SQLITE"] = "1"  # New critical flag
# =================================

def main():
    st.title("ChromaDB in Streamlit Cloud")
    
    with st.spinner("Initializing ChromaDB..."):
        try:
            # Delayed import after environment config
            import chromadb
            from chromadb.config import Settings
            
            # Initialize with explicit settings
            client = chromadb.Client(Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=None  # Disable disk persistence
            ))
            
            # Test functionality
            collection = client.create_collection("streamlit_test")
            collection.add(
                documents=["This is working in Streamlit Cloud!"],
                ids=["doc1"]
            )
            
            st.success(f"✅ Success! Collection count: {collection.count()}")
            st.balloons()
            
        except Exception as e:
            st.error(f"Initialization failed: {str(e)}")
            st.markdown("""
            **Immediate Fixes:**
            1. Update your `requirements.txt` exactly as shown below
            2. Clear cache via ☰ → Settings → Clear cache
            3. Redeploy the application
            """)

if __name__ == "__main__":
    main()
