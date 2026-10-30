from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a framework for building LLM applications.

It provides document loaders and text splitters.

It also supports vector databases and retrieval.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print("----------")