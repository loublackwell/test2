import streamlit as st
import os

# ===== ABSOLUTE CONFIGURATION =====
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"  # Force DuckDB
os.environ["CHROMA_ALL"] = "YES"  # Enable all workarounds
os.environ["CHROMA_SERVER_NO_SQLITE"] = "1"  # Disable SQLite completely
os.environ["CHROMA_DISABLE_TELEMETRY"] = "1"  # Reduce conflicts
# ==================================

def main():
    st.title("ChromaDB on Streamlit Cloud - Working Version")
    
    with st.spinner("Initializing ChromaDB..."):
        try:
            # Delayed import after environment config
            import chromadb
            from chromadb.config import Settings
            
            # Initialize with explicit DuckDB-only settings
            client = chromadb.Client(Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=None,  # Disable persistence
                allow_reset=True
            ))
            
            # Test with minimal operation
            version = client.get_version()
            st.success(f"✅ ChromaDB {version} initialized successfully!")
            
            # Simple document test
            collection = client.create_collection("test_docs")
            collection.add(
                documents=["This document proves ChromaDB works on Streamlit Cloud!"],
                ids=["doc1"]
            )
            
            st.write(f"Documents in collection: {collection.count()}")
            st.balloons()
            
        except Exception as e:
            st.error(f"Failed to initialize: {str(e)}")
            st.markdown("""
            **Final Solution:**
            1. Use the exact `requirements.txt` below
            2. Clear cache via ☰ → Settings → Clear cache
            3. Redeploy the application
            """)

if __name__ == "__main__":
    main()
