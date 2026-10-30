import os
from dotenv import load_dotenv

from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

# Create embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Create semantic splitter
splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile"
)

text = """
Python is a programming language.
It is widely used for web development.

The Earth revolves around the Sun.
The Sun is the center of our solar system.
"""

# Split text
documents = splitter.create_documents([text])

for doc in documents:
    print(doc.page_content)