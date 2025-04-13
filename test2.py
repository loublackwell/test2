import streamlit as st
import os

# Set up the environment before any imports
os.environ["CHROMA_FORCE_PYSQLITE"] = "1"  # Force pysqlite3 usage

def main():
    st.title("ChromaDB SQLite Version Check")
    
    with st.spinner("Loading ChromaDB and checking SQLite version..."):
        try:
            import chromadb
            import sqlite3
            
            # Display version info
            version = sqlite3.sqlite_version
            st.subheader("SQLite Version")
            st.code(version)
            
            # Version compatibility check
            if tuple(map(int, version.split("."))) >= (3, 35, 0):
                st.success("✅ SQLite version is compatible with ChromaDB")
            else:
                st.warning(f"⚠️ SQLite {version} may cause issues (needs 3.35.0+)")
            
            # Test ChromaDB functionality
            client = chromadb.Client()
            test_collection = client.create_collection("test_streamlit")
            test_collection.add(
                documents=["This is a test document"],
                ids=["doc1"]
            )
            st.success(f"ChromaDB working! Collection count: {test_collection.count()}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Try adding 'pysqlite3-binary' to requirements.txt")

if __name__ == "__main__":
    main()
