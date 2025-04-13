import streamlit as st
import os

# ===== CRITICAL CONFIG =====
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"
os.environ["CHROMA_ALL"] = "YES"
os.environ["CHROMA_SERVER_NO_SQLITE"] = "1"
os.environ["CHROMA_DISABLE_TELEMETRY"] = "1"  # New addition
# ===========================

def main():
    st.title("Working ChromaDB in Streamlit Cloud")
    
    with st.spinner("Initializing..."):
        try:
            # Delayed imports
            import chromadb
            from chromadb.config import Settings
            
            # Initialize with minimal settings
            client = chromadb.Client(Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=None,
                anonymized_telemetry=False
            ))
            
            # Test with simplest possible operation
            version = client.get_version()
            st.success(f"✅ ChromaDB {version} working!")
            st.balloons()
            
        except Exception as e:
            st.error(f"Initialization failed: {str(e)}")
            st.markdown("""
            **Nuclear Option:**
            1. Create a brand new GitHub repository
            2. Copy ONLY these two files:
              - `app.py` (this exact code)
              - `requirements.txt` (below)
            3. Create new Streamlit app from scratch
            """)

if __name__ == "__main__":
    main()
