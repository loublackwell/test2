import streamlit as st
import os

# Set the environment variable BEFORE importing chromadb
os.environ["CHROMA_DB_IMPL"] = "chroma_inmemory"

import chromadb

# Now you can use chromadb without issues
# Example:
client = chromadb.Client() #client will be in memory.
